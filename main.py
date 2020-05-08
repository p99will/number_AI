from silence_tensorflow import silence_tensorflow
silence_tensorflow()
from gui import *
from nn_class import *
import os,sys
import easygui
import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
print(tf.config.experimental.list_physical_devices('GPU'))

test_data = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
test_answer = [1]
model = tf.keras.models.Sequential()  # a basic feed-forward model

# mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
# (x_train, y_train),(x_test, y_test) = mnist.load_data()  # unpacks images to x_train/x_test and labels to y_train/y_test
box_num=20
boxes = []
windowsize = (300,350)

window1 = python_GUI("test1",windowsize)


box_size = windowsize[0] / box_num
test_number = 0
test_count = 0
# training_itterations = 10000
ai_datafile = "ai_data20-20-2.txt"

AI_TRAIN = True

def keras_train(x_train,y_train):
    model.add(tf.keras.layers.Dense(128, input_dim=box_num*box_num, activation=tf.nn.relu))  # takes our 28x28 and makes it 1x784
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
    model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution

    model.compile(optimizer='adam',  # Good default optimizer to start with
                  loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
                  metrics=['accuracy'])  # what to track

    model.fit(x_train, y_train, epochs=1000)  # train the model

    # val_loss, val_acc = model.evaluate(test_data, test_answer)  # evaluate the out of sample data with model
    # print("loss: " + str(val_loss))  # model's loss (error)
    # print("accuracy: " + str(val_acc))  # model's accuracy



# nn1 = NeuralNetwork()

def think_test(obj=None):
    x_test = check_boxes()

    predictions = model.predict([x_test])
    for i in range(0,10):
        print(str(i) + " : " + str("{:.7f}".format(predictions[0][i])))


    print('\n')

def nn_train(obj=None):
    data = []
    answers = []

    f=open(ai_datafile, 'r')
    raw_d = f.read().splitlines()
    f.close()

    for i in raw_d:
        i=i.split(':')
        answers.append(int(i[0]))

        i=i[1].split(',')
        tmp = []
        for ii in i:
            if ii != '':
                tmp.append(int(ii))
        data.append(tmp)

    x_train = data
    y_train = answers

    keras_train(x_train,y_train)
    # data = np.array(data)
    # answers = np.array(answers).T
    # nn1.train(data,answers,training_itterations)

def save_number(data,number):
    # val_loss, val_acc = model.evaluate(data, number)  # evaluate the out of sample data with model
    # print("loss: " + str(val_loss))  # model's loss (error)
    # print("accuracy: " + str(val_acc))  # model's accuracy
    text = str(number) + ":"
    for i in data:
        text += str(i) + ','
    f=open(ai_datafile,'a')
    f.write(text + '\n')
    f.close()

def clicked_box(obj):
    obj.color=colors.green
    obj.thickness=0
    obj.highlighted=True
    obj.visible=True

def reset_boxes(obj=None):
    for i in boxes:
        i.highlighted = 0
        i.color = colors.white
        i.thickness = 1
        i.visible=False

def check_boxes():
    ai_input=[]
    for i in boxes:
        is_highlited=0
        if hasattr(i, 'highlighted'):
            if (i.highlighted):
                is_highlited=1
        ai_input.append(is_highlited)
    return ai_input

def clicked_button1(obj):
    global test_count,test_number
    ai_input = check_boxes()
    if AI_TRAIN:
        # num = input("What Number is this?: ")
        # num = int(easygui.enterbox("What Number is this?"))
        num = test_number
        save_number(ai_input,num)
        test_count += 1
        if test_count >= 10:
            test_count = 0
            test_number += 1
            if test_number >= 10:
                test_number = 0
        print("Draw " + str(10-test_count) + ' x number: ' + str(test_number))
    reset_boxes()


for y in range(box_num):
    for x in range(box_num):
        box=shape("Box"+str(x)+':'+str(y),box_size*x,box_size*y,box_size,box_size,1)
        box.onDrag=clicked_box
        boxes.append(box)

start_pos = windowsize[1]-50

button1 = shape("Button1",0,start_pos,50,50,0,colors.blue)
button2 = shape("Reset",50,start_pos,50,50,0,colors.red)
button3 = shape("Think",100,start_pos,50,50,0,colors.green)
button4 = shape("Train",150,start_pos,50,50,0,colors.white)

button1.onclick=clicked_button1
button2.onclick=reset_boxes
button3.onclick=think_test
button4.onclick=nn_train

window1.add_custom_sprite(button1)
window1.add_custom_sprite(button2)
window1.add_custom_sprite(button3)
window1.add_custom_sprite(button4)

for i in boxes:
    window1.add_custom_sprite(i)

print("draw 10 number '0'")
while 1:
    window1.tick()

Introduction

In this project, we have developed a deep learning model to achieve a near state-of-the-art performance. We have used Keras and Tensorflow.

MNIST Dataset
We have cloned the dataset from Github.
Link: https://github.com/machinecurve/extra_keras_datasets.git


Model Building and Training  

We have built the model using Keras and used its capability of creating a convolutional neural network to increase the accuracy of the model. We added various CNN layers to the model and tested it. The model cannot differentiate between the lowercase and the uppercase of an alphabet which looks similar( For example w, m).



Connecting the front end to the model and Deployment   

Using javascript and flask, we were able to capture the handwritten character and send it to the model which predicted the character and returned the label value, using which the flask was able to display the letter.




 

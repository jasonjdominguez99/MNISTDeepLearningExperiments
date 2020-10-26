# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 22:02:26 2020

@author: Jason
"""

import matplotlib.pyplot as plt

def plot_accuracy_two_models(history1, model1_name, history2, model2_name, file_save_path):
    
    acc1 = history1.history['accuracy']
    val_acc1 = history1.history['val_accuracy']
    acc2 = history2.history['accuracy']
    val_acc2 = history2.history['val_accuracy']

    epochs = range(len(acc1))

    plt.figure(figsize=(10,9))

    plt.subplot(2,1,1)
    plt.plot(epochs, acc1, 'r', label="Training Accuracy for" + str(model1_name))
    plt.plot(epochs, acc2, 'b', label="Training Accuracy for" + str(model1_name))
    plt.title('Training accuracy compared among two models')
    plt.legend(loc=0)
    plt.grid(True)
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")

    plt.subplot(2,1,2)
    plt.plot(epochs, val_acc1, 'r', label="Validation Accuracy for" + str(model1_name))
    plt.plot(epochs, val_acc2, 'b', label="Validation Accuracy for" + str(model1_name))
    plt.title('Validation accuracy compared among two models')
    plt.legend(loc=0)
    plt.grid(True)
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")

    plt.savefig(file_save_path)
    plt.show()
    
    return None
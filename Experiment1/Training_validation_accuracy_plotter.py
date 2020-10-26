# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:42:06 2020

@author: Jason
"""
import matplotlib.pyplot as plt

def plot_train_val_accuracy(history, file_save_path):
    
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))

    plt.figure(figsize=(10,9))

    plt.subplot(2,1,1)
    plt.plot(epochs, acc, 'r', label="Training Accuracy")
    plt.plot(epochs, val_acc, 'b', label="Validation Accuracy")
    plt.title('Training and validation accuracy')
    plt.legend(loc=0)
    plt.grid(True)
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")

    plt.subplot(2,1,2)
    plt.plot(epochs, loss, 'r', label="Training Loss")
    plt.plot(epochs, val_loss, 'b', label="Validation Loss")
    plt.title('Training and validation loss')
    plt.legend(loc=0)
    plt.grid(True)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")

    plt.savefig(file_save_path)
    plt.show()
    
    return None
    
# Synthetic-Data-using-GAN-and-Stable-Diffusion
<h2>UNDER CONSTRUCTION</h2>

<h3>IDC DATASET</h3>
The dataset comprised 277,524 image patches of 50 x 50 pixels which were extracted from the WSIs. The WSIs included 198,738 non-IDC (negative) and 78,786 IDC (positive) diagnoses.
<h2></h2>
Firstly, we wrote some code by creating "file_directory_changer_and_class_seperater.py" file for changing directory and seperating all classes.
Secondly, we plan to generate synthetic dataset using genarative models for each class. Then, we wil combine them real dataset and combine them every classes.
In this way, we will have created all the datasets we will use.

<h2>The next steps are normalization and image size adjustment and use in the classification model.</h2>

FID score will be calculated by evaluating the synthetic content datasets created in the CNN model.

Comparison of the performance of synthetic data in the breast cancer classification using GAN and Stable Diffusion

![overview](https://user-images.githubusercontent.com/117897880/229492793-2b2c3476-8766-4cf9-b214-cf787f3527f2.png)

<h2>Instances of generated images using DCGAN</h2>

Generated images will be here (Loading)

<h2>Instances of generated images using Stable Diffusion</h2>

Generated images will be here (Loading)

<h2>Steps of this project</h2>
 
<h3>1)Project Overview:</h3>

-Define the project's objective: To compare the accuracy and FID score of breast cancer classification using the IDC dataset with and without data augmentation techniques, specifically DCGAN and Stable Diffusion.

<h3>2)Dataset Preparation:</h3>

-Acquire the IDC dataset, ensuring it includes sufficient labeled images for training and evaluation.

-Preprocess the dataset: Normalize pixel values, resize images, and split the dataset into training and testing sets.

<h3>3)Baseline Model Development:</h3>

-Implement a baseline breast cancer classification model without data augmentation techniques.

-Select a suitable classification algorithm, such as Convolutional Neural Networks (CNNs).

-Train the baseline model using the training dataset.

-Evaluate the model's accuracy using the testing dataset and record the results.

<h3>4)Data Augmentation with GANs:</h3>

-Implement GANs for data augmentation. Generate synthetic breast cancer images using the GAN model.

-Combine the original training dataset with the synthetic images created by the GAN.

-Retrain the breast cancer classification model using the augmented dataset.

-Evaluate the model's accuracy using the testing dataset and record the results.

<h3>5)Data Augmentation with Stable Diffusion:</h3>

-Implement Stable Diffusion as a data augmentation technique for breast cancer images.

-Apply the Stable Diffusion algorithm to generate augmented images.

-Combine the original training dataset with the augmented images.

-Retrain the breast cancer classification model using the augmented dataset.

-Evaluate the model's accuracy using the testing dataset and record the results.

<h3>6)Result Analysis and Comparison:</h3>

-Analyze and compare the accuracy and FID score results obtained from the baseline model, DCGAN-augmented model, and Stable Diffusion-augmented model.

-Calculate and compare relevant metrics such as accuracy, precision, recall, and F1 score for each model.

-Use appropriate statistical tests to determine the significance of the observed differences in accuracy.

<h3>7)Discussion and Conclusion:</h3>

-Discuss the findings from the comparison and analyze the impact of data augmentation techniques on breast cancer classification accuracy.

-Consider factors such as computational complexity, robustness, and generalization ability of the models.

-Summarize the advantages and limitations of using GANs and Stable Diffusion for data augmentation in breast cancer classification.

<h3>8)Documentation and Reporting:</h3>

-Prepare a comprehensive report documenting the project's methodology, results, and conclusions.

-Include visualizations such as accuracy graphs, confusion matrices, and comparative analysis charts.

-Provide detailed explanations of the implemented models, algorithms, and techniques.

-Consider sharing your findings with the scientific community through publications or presentations.

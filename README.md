# Based on CRF to extract evaluation objects and evaluation words and form a system development for visual display
## first part-generate the CRF model
1、Provide semEval2014-laptops and restaurants original data set and processed data set
2、Provide the original code for processing data and the code for system construction
3、Provide the template used in this experiment

### dataset
provide:
1、original dataset
2、All comment sentences of the separately extracted data set (evaluation objects are capitalized)
3、Processed dataset

### process
First call label.py to label the processed data set, and then divide the labeled data set into a training set and a test set. Input the training set into CRF++0.58 to train the model, then call the trained model to mark the test set, and finally call test.py to test the accuracy, precision, recall, and F1 value of the model.


## second part-Introduction to System Development
choose the model performed best as the final model and then begin to develope a visiual system:
  we adopted the conventional c/s model for development. The system is designed to process English comment sentences, extract evaluation words and evaluation objects from them and visually present the core content of the comment sentences. The development environment we chose was IDEA, and the development language was JavaScript.
  the front-end page has two text area, input and output. user can enter a comment sentence and click 'start', then the system will process it (like we do above,the system call the funtions and model to generate pairs),finally, the opinion target and opinion word will show in the 'output'.

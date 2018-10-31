# Artificial-Neural-Network

Step 1:
  Extract the data and divide into x_trn,y_trn,x_tst,y_tst
  
Step 2:
  If your data is images then flatten it to the required size
  
Step 3:
  Before giving the x_trn to the fit, normalize the points by dividing it by 255.
  
Step 4:
  The input to the first layer should be the sixe of columns/features in x_trn
  
Step 5:
  Change the values of number of neurons/nodes and add/delete the layers until you find a appropriate accuracy for the testing data.

Step 6:
  The training accuracy will be 100% since you are doing a classification model, if not then no need to get it to 100% as long as your testing accuracy is the maximum you can get for any combination.
  
Step 7:
  The batch size defines the number of times the weights get updated and epochs decides the number of iterations.

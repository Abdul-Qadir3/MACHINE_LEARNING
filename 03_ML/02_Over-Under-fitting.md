## `Over fitting and Under fitting`
![alt text](image-14.png)

<br>
<br>
- Always use `generalize model` to work on the unknown data

![alt text](image-15.png)
### Overfitting:
- Model performs well on training data but poorly on test/unseen data
  - High bias, low variance

### Overfitting:
- More `parameters` => more chances of overfitting than underfitting
  - R`egularization` techniques can help in reducing overfitting by adding a penalty term to loss function or using dropout
  - `Regularization` techniques (Ridge, Lasso, ElasticNet) can help in reducing the number of parameters which helps in avoiding
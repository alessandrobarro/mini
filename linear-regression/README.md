this code implements linear regression, one of the fundamental linear models in ML.

The input dataset is provided from the user, who decides the number of features per example.

The user must also provide data regarding the outcomes correlated to the examples (since the linear regression falls in the category of supervised learning models)
and no less than intances, learning grade for gradient descent optimization.

After the model's parameters are trained (theta), the prediciton can be made in the form y = theta^T x + epsilon, where epsilon corresponds to the overall maximum
accuracy error of the model, calculated with a normal gaussian probability density function (whose parameters and standard deviation are elaborated directly from
the given data).

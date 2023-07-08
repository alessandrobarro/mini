This code implements linear regression, one fundamental linear model in ML.

The input dataset is provided by the user, who decides the number of features per example.

The user must also provide data regarding the outcomes correlated to the examples such as the number of intances (iterations) and learning grade (for gradient descent optimization).

After the model's parameters are trained (theta), the prediction can be made in the form y = theta^Tx + epsilon, where epsilon corresponds to the overall maximum
accuracy error of the model, calculated with a normal gaussian probability density function (whose parameters and standard deviation are elaborated directly from
the given data).

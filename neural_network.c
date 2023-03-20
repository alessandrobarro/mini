/* Librerie utilizzate */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* Costanti intere */
#define WEIGHT_NMAX 11
#define T_T 5 //theta threshold (soglia per la funzione di attivazione)
#define N_IN 2 //numero di input
#define N_H_N 2 //numero di nodi nascosti
#define N_OUT 1 //numero di output
#define N_T_S //numero dei set di "training" della rete
#define EPOCHS 10000 //numero di iterazioni totali del "training"

/* Prototipi */
double sigmoid(double);
double d_sigmoid(double);

int main(int argc, char * argv[])
{
    double hidden_layer[N_H_N];
    double output_layer[N_OUT];

    double hidden_layer_bias[N_H_N];
    double output_layer_bias[N_OUT];

    double hidden_weights[N_IN][N_H_N];
    double output_weights[N_H_N][N_OUT];

    double training_inputs[N_T_S][N_IN] = {{0.0f, 0.0f}, {1.0f, 0.0f}, {0.0f, 1.0f}, {1.0f, 1.0f}};
    double training_outputs[N_T_S][N_OUT] = {{0.0f}, {1.0f}, {1.0f}, {0.0f}};

    int training_set_order[] = {0, 1, 2, 3};
    int i, j, m, n, k, x;

    n = 0;
    while(n < EPOCHS){
        shuffle(training_set_order, N_T_S);
        x = 0;
        while(x < N_T_S){
            i = training_set_order[x];
            x++;
        }
        n++;
    }

    /* Calcolo dell'attivazione dell'output layer */
    for(j = 0; j < N_H_N; j++){ //j numero di nodi in output
        double activation = hidden_layer_bias[j];
        for(k = 0; k < N_IN; k++){ //numero di nodi nascosti
            activation += training_inputs[i][k] * hidden_weights[k][j];
        }
        hidden_layer[j] = sigmoid(activation);
    }

    for(j = 0; j < N_H_N; j++){ //j numero di nodi in output
        double activation = output_layer_bias[j];
        for(k = 0; k < N_IN; k++){ //numero di nodi nascosti
            activation += hidden_layer[k] * output_weights[k][j];
        }
        output_layer[j] = sigmoid(activation);
    }

    /* Calcolo del cambio dei pesi in output*/
    double delta_output[N_OUT];
    for(j = 0; j < N_OUT; j++){
        double dError = (training_outputs[i][j] - output_layer[j]);
        delta_output[j] = dError * d_sigmoid(output_layer[j]);
    }

    double deltaHidden[N_H_N];
    for (j = 0; j < N_H_N; j++){
        double dError = 0.0f;
        for(k = 0; k < N_OUT; k++){
            dError += delta_output[k] * output_weights[j][k];
        }
        deltaHidden[j] = dError * d_sigmoid(hidden_layer[j]);
    }

    for (j = 0; j < N_OUT; j++){
        output_layer_bias[j] += delta_output[j] * lr;
        for(k = 0; k < N_H_N; k++){
            output_weights[k][j] += hidden_layer[k] * delta_output[j] * lr;
        }
    }

    for (j = 0; j < N_H_N; j++){
        hidden_layer_bias[j] += deltaHidden[j] * lr;
        for(k = 0; k < N_IN; k++){
            hidden_weights[k][j] += training_inputs[i][k] * deltaHidden[j] * lr;
        }
    }

    for(i = 0; i < N_OUT; i++){
        for(j = 0; j < N_H_N; j++){
            printf("%f", output_weights[j][i]);
        }
    }

    return 0;
}


/* Funzione di attivazione */
double sigmoid(double n)
{
    return 1 / (1 + exp(-n));
}

/* Derivata della funzione di attivazione */
double d_sigmoid(double n)
{
    return n * (1 - n);
}
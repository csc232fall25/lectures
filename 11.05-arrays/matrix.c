#include <stdlib.h>
#include <stdio.h>

int *mcreate(int);
int *mmult(int *, int *, int);

int main(int argc, char *argv[]) {
    int n, *mat_a, *mat_b, *mat_c;

    n = strtol(argv[1], NULL, 10);
    mat_a = mcreate(n);
    mat_b = mcreate(n);
    mat_c = mmult(mat_a, mat_b, n);

    free(mat_a);
    free(mat_b);
    free(mat_c);

    return 0;
}

/* mcreate: Creates an n x n matrix of random one-digit integers. */
int *mcreate(int n) {
    int i, j, *mat;

    mat = (int *)calloc(sizeof(int), n * n);

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            mat[i * n + j] = rand() % 10;
        }
    }

    return mat;
}

/* mmult: Multiplies two n x n matrices. */
int *mmult(int *mat_a, int *mat_b, int n) {
    int i, j, k, *mat_c;

    mat_c = (int *)calloc(sizeof(int), n * n);

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            for (k = 0; k < n; k++) {
                mat_c[i * n + j] += mat_a[i * n + k] * mat_b[k * n + j];
            }
        }
    }

    return mat_c;
}

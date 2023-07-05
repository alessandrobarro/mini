/*Accessory libraries*/
#include <stdio.h>
#include <stdlib.h>

/*Constant values*/
#define NREC 9
#define NCOL 9

/*coord variable type, used in insertscheme()*/
typedef struct{
    int x, y, data;
}coord;

/*Function prototypes*/
void insertscheme(int [][NCOL]);
void sudokudisplay(int [][NCOL]);
int findsol(int[][NCOL], int, int);
int unique(int[][NCOL], int, int, int);
int sudoku(int [][NCOL]);

/*Empty starting matrix*/
int mat[NREC][NCOL] = {{0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0},
                        {0,0,0,0,0,0,0,0,0}};

/*main() - primary function*/
int main(int argc, char * argv[])
{
    int choice;
    int i, j, val;

    printf("Sudoku bot\n");
    printf("\n");
    sudokudisplay(mat);
    printf("\n");

    insertscheme(mat);
    printf("\n");
    sudokudisplay(mat);
    printf("\n");

    if(sudoku(mat)){
        printf("The game scheme inserted is valid\n");
        printf("Finding a solution...\n");
        if(findsol(mat, 0, 0))
            sudokudisplay(mat);
            printf("\n");
            printf("Is the solution of the input game scheme\nPlease, restart the script");
    }
    else
        printf("The game scheme inserted is not valid, please restart\n");

    return 0;
}

/*sudokudisplay() - displays the matrix to the user*/
void sudokudisplay(int mat[][NCOL])
{
    int i, j;

	for(i = 0; i < NREC; i++){
	    for(j = 0; j < NCOL; j++){
	       printf("%d ", mat[i][j]);
	    }
	    printf("\n");
	}

    return;
}

/*insertscheme() - inserts the values prompted to the user in the matrix*/
void insertscheme(int mat[][NCOL]){
    coord pos;
    int i, j;
    
    printf("Insert the scheme (insert '0 0 0' to stop the acquisition)\n");
    printf("Type in the following structure: [RECORD] [COLUMN] [VALUE]\n");
    scanf("%d %d %d", &pos.x, &pos.y, &pos.data);

    pos.x--;
    pos.y--;
    
    while(pos.x != -1 && pos.y != -1 && pos.data != -1){
        for(i = 0; i < NREC; i++){
            for(j = 0; j < NCOL; j++){
                if(i == pos.x && j == pos.y)
                    mat[i][j] = pos.data;
            }
        }
        scanf("%d %d %d", &pos.x, &pos.y, &pos.data);
        pos.x--;
        pos.y--;
    }

    return;
}

/*sudoku() - checks if the inserted scheme is valid*/
int sudoku(int mat[][NCOL])
{
    int val, count, i, j, n, m, k, l, sudoku, sudokurec, sudokucol, sudokucell;

    sudokurec = 1;
    sudokucol = 1;
    sudokucell = 1;

    for(i = 0; i < NREC; i++){
        for(j = 0; j < NCOL; j++){
            if(mat[i][j] != 0){
                for(n = i + 1; n < NREC; n++){
                    if(mat[i][j] == mat[n][j])
                        sudokurec = 0;
                }
                for(m = j + 1; m < NCOL; m++){
                    if(mat[i][j] == mat[i][m])
                        sudokucol = 0;
                }
            }
        }
    }

    for(n = 0; n < 9; n = n + 3){
        for(m = 0;  m < 9; m = m + 3){
            for(i = n; i < n + 3; i++){
                for(j = m; j < m + 3; j++){
                    if(mat[i][j] != 0){
                        for(k = i + 1; k < NREC; k++){
                            if(mat[i][j] == mat[k][j])
                                sudokucell = 0;
                        }
                        for(l = j + 1; l < NCOL; l++){
                            if(mat[i][j] == mat[i][l])
                                sudokucell = 0;
                        }
                    }
                }
            }
        }
    }
    
    if(sudokurec && sudokucol && sudokucell)
        sudoku = 1;
    else
        sudoku = 0;

    return sudoku;
}

/*unique() - checks if the value in the corrisponding coordinates distinguishes from the other numbers*/
int unique(int mat[][NCOL], int nr, int nc, int n)
{
    int nr_s = (nr/3) * 3;
    int nc_s = (nc/3) * 3;
    int i, j, res;

    res = 1;

    for(i = 0; i < 9; i++){
        if (mat[nr][i] == n)
            res = 0;
        if (mat[i][nc] == n)
            res = 0;
        if (mat[nr_s + (i % 3)][nc_s + (i/3)] == n)
            res = 0;
    }

    return res;
}

/*findsol() - finds the correct values and overwrites the initial matrix (works in synergy with unique())*/
int findsol(int mat[][NCOL], int nr, int nc)
{
    int i;

    if((nr < 9) && (nc < 9)){
        if(mat[nr][nc] != 0){
            if((nc + 1) < 9)
                return findsol(mat, nr, nc + 1);
            else if((nr + 1) < 9)
                return findsol(mat, nr + 1, 0);
            else
                return 1;
        }
        else
        {
            for(i = 0; i < 9; i++){
                if(unique(mat, nr, nc, i + 1)){
                    mat[nr][nc] = i + 1;
                    if((nc + 1) < 9){
                        if(findsol(mat, nr, nc + 1))
                            return 1;
                        else
                            mat[nr][nc] = 0;
                    }
                    else if((nr + 1) < 9){
                        if(findsol(mat, nr + 1, 0))
                            return 1;
                        else
                            mat[nr][nc] = 0;
                    }
                    else
                        return 1;
                }
            }
        }
        return 0;
    
    return 1;
    }
}
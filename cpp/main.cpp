#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>

using namespace std;

const int MAXN = 1000;

int N, M;
char labyrinth[MAXN][MAXN];
bool visited[MAXN][MAXN];
int order[MAXN][MAXN];

// Returns true if the cell (i, j) is a valid hole
bool valid(int i, int j) {
    return i >= 0 && i < N && j >= 0 && j < M && labyrinth[i][j] == '.';
}

// Recursive DFS function to find the longest paths
void dfs(int i, int j, int& length, int& max_order) {
    visited[i][j] = true;
    order[i][j] = max_order++;
    length++;
    // vertical、horizontal and diagonal directions
    static const int di[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    static const int dj[] = {-1, 0, 1, -1, 1, -1, 0, 1};
    for (int k = 0; k < 8; k++) {
        int ni = i + di[k];
        int nj = j + dj[k];
        if (valid(ni, nj) && !visited[ni][nj]) {
            dfs(ni, nj, length, max_order);
        }
    }
}

// Use DFS to solve this problem
int main(int argc, char** argv) {
    // Read labyrinth from file
    ifstream fin(argv[1]);

    // Get labyrinth shape
    int i = 0;
    while (!fin.eof()) {
        fin >> labyrinth[i];
        i++;
    }
    N = i;
    M = strlen(labyrinth[0]);

    // Print labyrinth
    cout<< "input:" << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cout << labyrinth[i][j];
        }
        cout << endl;
    }

    int max_length = 0;
    int max_order = 0;
    
    // find each entrance
    for (int j = 0; j < M; j++) {
        if (valid(0, j)) {
            int length = 0;
            dfs(0, j, length, max_order);
            if (length > max_length) {
                max_length = length;
            }
        }
    }

    bool result_is_legal = false;
    // valid the length is legal
    for (int j = 0; j < M; j++) {
        if(labyrinth[N - 1][j] != '#') {
            result_is_legal = true;
        }
    }

    cout << "output:" << endl;
    if (max_length == 0 || !result_is_legal) {
        cout << -1 << endl;
    } else {
        cout << max_length << endl;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (visited[i][j]) {
                    cout << order[i][j];
                } else {
                    cout << labyrinth[i][j];
                }
            }
            cout << endl;
        }
    }

    return 0;
}

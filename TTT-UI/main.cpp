#include "mainwindow.h"
#include "board.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    //w.close();

    Board board;
    board.show();
    board.InitializeBoard();

    return a.exec();
}

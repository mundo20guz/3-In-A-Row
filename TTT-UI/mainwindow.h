#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:

    //Do not modify these yet.
    explicit MainWindow(QWidget *parent = nullptr);       
    ~MainWindow();

    //User-defined public functions/proprerties.
    void FillBoardRandomly();
    void InitializeWindow();


private:

    //Do not modify these yet.
    Ui::MainWindow *ui;
    void InitializeText();

    //User-defined private functions/properties.

};

#endif // MAINWINDOW_H

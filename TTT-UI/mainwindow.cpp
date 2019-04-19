#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QtTest/QTest>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->InitializeText();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::InitializeText()
{
    QList<QLabel *> allLabels = ui->centralWidget->findChildren<QLabel *>();

    for(int i = 0; i < allLabels.count(); i++)
    {
        allLabels.at(i)->setText("");
    }
}

void MainWindow::FillBoardRandomly()
{
    QList<QLabel *> allLabels = ui->centralWidget->findChildren<QLabel *>();

    for(int i = 0; i < allLabels.count(); i++)
    {
        const int randomBit = rand() % 2;

        if(randomBit == 0)
        {
            allLabels.at(i)->setText("X");
        }
        else {
            allLabels.at(i)->setText("O");
        }


        QTest::qWait(250);
    }
}

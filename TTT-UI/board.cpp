#include "board.h"
#include "ui_board.h"
#include "tile.h"
#include <QtDebug>

Board::Board(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Board)
{
    ui->setupUi(this);
    this->setWindowTitle("Board");

}

Board::~Board()
{
    delete ui;
}

void Board::InitializeBoard()
{
    //Set the grid layout to overlap the board form (take up the whole page).
    QRect geom = this->geometry();

    ui->mainGrid->setGeometry(geom);

//    ui->mainGrid->geometry().setWidth(geom.width());
//    ui->mainGrid->geometry().setHeight(geom.height());
//    ui->mainGrid->geometry().setX(geom.x());
//    ui->mainGrid->geometry().setY(geom.y());
    qDebug("%d", geom.x());
    qDebug("%d", geom.y());
    qDebug("%d", geom.width());
    qDebug("%d", geom.height());
    qDebug("-");
    qDebug("%d", ui->mainGrid->geometry().x());
    qDebug("%d", ui->mainGrid->geometry().y());
    qDebug("%d", ui->mainGrid->geometry().width());
    qDebug("%d", ui->mainGrid->geometry().height());


    //Add the tiles to the board.
    int tileCount = 0;
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            //Create a new tile object and add it to the list.
            Tile *tmp = new Tile(this, tileCount);
            this->tiles.append(tmp);

            //Get the tile from the list, add it to the board. Adjust geometry.
            //ui->mainGrid->addWidget(tmp, i, j);
            ui->mainGrid->addWidget(tmp, i, j);

//            switch(i % 2)
//            {
//                case 0:
//                    ui->mainGrid->itemAtPosition(i,j)->setAlignment(Qt::AlignBottom);
//                break;
//            case 1:
//                    ui->mainGrid->itemAtPosition(i,j)->setAlignment(Qt::AlignVCenter);
//                break;
//            case 2:
//                    ui->mainGrid->itemAtPosition(i,j)->setAlignment(Qt::AlignTop);
//                break;
//            }

//            switch(j % 2)
//            {
//                case 0:
//                    ui->mainGrid->itemAtPosition(i,j)->setAlignment(Qt::AlignRight);
//                break;
//                case 1:
//                    ui->mainGrid->itemAtPosition(i,j)->setAlignment(Qt::AlignHCenter);
//                break;
//                case 2:
//                    ui->mainGrid->itemAtPosition(i,j)->setAlignment(Qt::AlignLeft);
//                break;
//            }

        }
    }

    qDebug("The number of tiles created: %d",this->tiles.count());
    qDebug("The number of children mainGrid claims to have is: %d", ui->mainGrid->children().count());
    qDebug("The number of children board claims to have is: %d", this->children().count());

}

#include "tile.h"
#include "ui_tile.h"

Tile::Tile(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Tile)
{
    ui->setupUi(this);
}

Tile::Tile(QWidget *parent, int tileId) :
    QWidget(parent),
    ui(new Ui::Tile)
{
    ui->setupUi(this);
    this->tileId = tileId;
}

Tile::~Tile()
{
    delete ui;
}

void Tile::setTileId(int id)
{
    tileId = id;
}

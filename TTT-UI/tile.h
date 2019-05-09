#ifndef TILE_H
#define TILE_H

#include <QWidget>

namespace Ui {
class Tile;
}

class Tile : public QWidget
{
    Q_OBJECT

public:
    explicit Tile(QWidget *parent = nullptr);
    ~Tile();
    explicit Tile(QWidget *parent = nullptr, int tileId = 0);

    //User-defined functions.
    int getTileId();
    void setTileId(int id);

private:
    Ui::Tile *ui;
    int tileId;
};

#endif // TILE_H

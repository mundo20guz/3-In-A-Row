#ifndef BOARD_H
#define BOARD_H

#include <QWidget>
#include "tile.h"

namespace Ui {
class Board;
}

class Board : public QWidget
{
    Q_OBJECT

public:
    explicit Board(QWidget *parent = nullptr);
    ~Board();

    void InitializeBoard();


private:
    Ui::Board *ui;
    QList<Tile*> tiles;



};

#endif // BOARD_H

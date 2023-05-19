#include "box.h"
using namespace std;

//**********************************************************
// setWidthBox assigns a value to the widthBox member.     *
//**********************************************************

void Box::setWidthBox(double widb)
{
    widthBox = widb;
}

//**********************************************************
// setLengthBox assigns a value to the lengthBox member.   *
//**********************************************************

void Box::setLengthBox(double lenBox)
{
    lengthBox = lenBox;
}

//**********************************************************
// setHeightBox assigns a value to the heightBox member.   *
//**********************************************************

void Box::setHeightBox(double hgtBox)
{
    heightBox = hgtBox;
}

//**********************************************************
// getWidthBox returns the value in the widthBox member.   *
//**********************************************************

double Box::getWidthBox() const
{
    return widthBox;
}

//**********************************************************
// getLengthBox returns the value in the lengthBox member. *
//**********************************************************

double Box::getLengthBox() const
{
    return lengthBox;
}

//**********************************************************
// getHeightBox returns the value in the heightBox member. *
//**********************************************************

double Box::getHeightBox() const
{
    return heightBox;
}

//*************************************************************
// getVolume returns the product of width, length, and height.*
//*************************************************************

double Box::getVolume() const
{
    return (widthBox * lengthBox * heightBox);
}

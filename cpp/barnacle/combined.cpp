//James Atkins
//First coded 10-02-2021
//This program demonstrates a class, uses multiple files for another class

int sample_test_method(double h, double w) {
    double area;
    area = h * w;
    return area;
}

#include <iostream>

using namespace std;
#ifndef BOX_H
#define BOX_H

//Box class declaration
class Box
{
    private:
        double widthBox;
        double lengthBox;
        double heightBox;
    public:
        void setWidthBox(double);
        void setLengthBox(double);
        void setHeightBox(double);
        double getWidthBox() const;
        double getLengthBox() const;
        double getHeightBox() const;
        double getVolume() const;
};

#endif // BOX_H_INCLUDED
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

//Rectangle class declaration
class Rectangle
{
    private:
        double width;
        double length;
    public:
        void setWidth(double);
        void setLength(double);
        double getWidth() const;
        double getLength() const;
        double getArea() const;
};

//****************************************************
// setWidth assigns a value to the width member.     *
//****************************************************

void Rectangle::setWidth(double w)
{
    width = w;
}

//****************************************************
// setLength assigns a value to the length member.   *
//****************************************************

void Rectangle::setLength(double len)
{
    length = len;
}

//****************************************************
// getWidth returns the value in the width member.   *
//****************************************************

double Rectangle::getWidth() const
{
    return width;
}

//****************************************************
// getLength returns the value in the length member. *
//****************************************************

double Rectangle::getLength() const
{
    return length;
}

//****************************************************
// getArea returns the product of width times length.*
//****************************************************

double Rectangle::getArea() const
{
    return (width * length);
}

//****************************************************
// Function main                                     *
//****************************************************

int main()
{
    Rectangle rectangle;   // Define an instance of the Rectangle class
    double rectWidth;      // Local variable for width
    double rectLength;     // Local variable for length

    Box someBox;           // Define an instance of the Box class
    double boxWidth;       // Local variable for box width
    double boxLength;      // Local variable for box length
    double boxHeight;      // Local variable for box height

    string input;          // Variable for start of program
    double boxArea;

    cout << "Would you like to find the area or the volume?" << endl;
    cout << "(1) Area" << endl;
    cout << "(2) Volume" << endl;
    cin >> input;
    if (input == "1")
    {
    // Rectangle calculation
    // Get the rectangle's width and length from the user
    // using input validation.
        cout << "This program will calculate the area of rectangle. What is the width?" << endl;
        cin >> rectWidth;
        while (rectWidth <= 0)
        {
            cout << "That is not possible. What is the width?" << endl;
            cin >> rectWidth;
        }
        rectangle.setWidth(rectWidth);

        cout << "What is the length?" << endl;
        cin >> rectLength;
        while (rectLength <= 0)
        {
            cout << "That is not possible. What is the length?" << endl;
            cin >> rectLength;
        }
        rectangle.setLength(rectLength);

    // Store the width and length of the rectangle
    // in the rectangle object.
    // Display the rectangle's data.
        cout << "Here is the rectangle's data:" << endl;
        cout << "Width: " << rectangle.getWidth() << endl;
        cout << "Length: " << rectangle.getLength() << endl;
        cout << "Area: " << rectangle.getArea() << endl;
        cout << endl;
    }
    else if (input == "2")
    {
    // Box Calculation
    // Get the rectangle's width, length, height, from the user
    // using input validation.
        cout << "This program will calculate the volume of a box. What is the width?" << endl;
        cin >> boxWidth;
        while (boxWidth <= 0)
        {
            cout << "That is not possible. What is the width?" << endl;
            cin >> boxWidth;
        }
        someBox.setWidthBox(boxWidth);

        cout << "What is the length?" << endl;
        cin >> boxLength;
        while (boxLength <= 0)
        {
            cout << "That is not possible. What is the length?" << endl;
            cin >> boxLength;
        }
        someBox.setLengthBox(boxLength);

        cout << "What is the height?" << endl;
        cin >> boxHeight;
        while (boxHeight <= 0)
        {
            cout << "That is not possible. What is the height?" << endl;
            cin >> boxHeight;
        }
        someBox.setHeightBox(boxHeight);

        boxArea = sample_test_method(boxHeight, boxWidth);

    // Store the width, length, height of the box
    // in the box object.
    // Display the box's data.
        cout << "Here is the rectangle's data:" << endl;
        cout << "Width: " << someBox.getWidthBox() << endl;
        cout << "Length: " << someBox.getLengthBox() << endl;
        cout << "Height: " << someBox.getHeightBox() << endl;
        cout << "Volume: " << someBox.getVolume() << endl;
    }

    return 0;
}

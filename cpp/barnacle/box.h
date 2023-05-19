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

# 三点坐标计算三角形面积

给出三角形三个定点的坐标：$(x_1,y_1),(x_2,y_2),(x_3,y_3)$，计算三角形面积

## 向量叉乘

三角形面积公式：$S=\frac{1}{2}ab \sin \theta=\frac{1}{2} \vec{a}\times \vec{b}$

$\vec{a}=(x^{'}_1, y^{'}_1)=(x_2-x_1,y_2-y_1),\vec{b}=({x^{'}_2},y^{'}_2)=(x_3-x_1,y_3-y_1)$

$S=\frac{1}{2}\lvert x^{'}_1y^{'}_2-x^{'}_2y^{'}_1 \rvert$

```java
    public double getTriArea(int x1, int y1, int x2, int y2, int x3, int y3){
        double x1_ = x2 - x1, y1_ = y2 - y1;
        double x2_ = x3 - x1, y2_ = y3 - y1;
        return Math.abs(x1_ * y2_ - x2_ * y1_) / 2;
    }
```


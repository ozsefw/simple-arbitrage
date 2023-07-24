$$ \frac{R_y}{R_x} = P_1 $$
$$ \frac{R_y - \Delta y}{R_x + F \Delta x} = P_2 $$

$$ R_y = P_1 R_x$$
$$ P_1 R_x - \Delta y = P_2 (R_x + F \Delta x)$$
$$ (P_1 - P_2)R_x  = P_2 F \Delta x + \Delta y$$
$$ R_x  = \frac{P_2 F \Delta x + \Delta y}{P_1 - P_2}$$

## uni_v3 liquidity的验证

$$ \Delta x = L \Delta \sqrt{\frac{1}{P}}$$


## v3获取 x，y

$$ x = \frac{xy}{y} $$
$$ x = \frac{\sqrt{xy}\sqrt{xy}}{y} $$
$$ x = L\frac{\sqrt{xy}}{\sqrt{y^2}} $$
$$ x = L\frac{1}{\sqrt{P}} $$

## v2计算
$\Delta x$

$$ (x + F\Delta x)(y-\Delta y)=xy $$
$$ (\Delta y)= y - \frac{xy}{x + F\Delta x} $$
$$ \Delta y= \frac{F\Delta x  y}{x + F\Delta x} $$

$\Delta y$
$$ (x - \Delta x)(y+F\Delta y) = xy $$
$$ \Delta x = \frac{xF\Delta y }{y+F\Delta y} $$
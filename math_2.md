A 是dex1， B是dex2

$$ A_x A_y = (A_x + \theta_A E_{in})(A_y - \Delta y )$$
$$ B_x B_y = (B_x - E_{out})(B_y + \theta_B \Delta y ) $$

$$ \Delta y  = A_y - \frac{A_x A_y}{A_x + \theta_A E_{in}} $$
$$ E_{out} = B_x - \frac{B_x B_y}{B_y + \theta_B \Delta y } $$

$$ E_{out} = \frac{ B_x \theta_B \Delta y}{ B_y + \theta_B \Delta y } $$

### replace $\Delta y$ in $E_{out}$ 2 
$$ \Delta y  = \frac{A_y \theta_A E_{in} }{A_x + \theta_A E_{in}} $$

$$ E_{out} = \frac{ B_x A_y \theta_B \theta_A E_{in} }{ B_y A_x + B_y \theta_A E_{in} + \theta_B A_y \theta_A E_{in} } $$

### replace $\Delta y$ in $E_{out}$ 3

### replace $\Delta y$ in $E_{out}$ 
$$ \Delta y  = \frac{A_y \theta_A E_{in} }{A_x + \theta_A E_{in}} $$

$$ E_{out} = B_x - \frac{B_x B_y}{B_y + \theta_B (\frac{A_y \theta_A E_{in} }{A_x + \theta_A E_{in}}) } $$
$$ E_{out} = B_x - \frac{B_x B_y (A_x + \theta_A E_{in})}{B_y (A_x + \theta_A E_{in}) + \theta_B (A_y \theta_A E_{in}) } $$
$$ E_{out} = B_x - \frac{B_x B_y A_x + B_x B_y \theta_A E_{in}}{B_y A_x + B_y \theta_A E_{in} + \theta_B A_y \theta_A E_{in} } $$
$$ E_{out} = \frac{ B_x \theta_B A_y \theta_A E_{in} }{B_y A_x + B_y \theta_A E_{in} + \theta_B A_y \theta_A E_{in} } $$

$$ p = E_{out} - E_{in} = \frac{ (B_x \theta_B A_y \theta_A E_{in}) }{B_y A_x + B_y \theta_A E_{in} + \theta_B A_y \theta_A E_{in} } - E_{in} $$

$$ p = E_{in} (\frac{ B_x \theta_B A_y \theta_A }{B_y A_x + B_y \theta_A E_{in} + \theta_B A_y \theta_A E_{in} } - 1) $$

$$ p = \frac{ B_x \theta_B A_y \theta_A E_{in} - E_{in} B_y A_x - E_{in} B_y \theta_A E_{in} - E_{in}\theta_B A_y \theta_A E_{in} }{B_y A_x + B_y \theta_A E_{in} + \theta_B A_y \theta_A E_{in} } $$
## draft

### calculate $\Delta y$
$$ A_x + \theta_A E_{in}  = \frac{A_x A_y}{A_y - \Delta y} $$
$$ {A_y - \Delta y}  = \frac{A_x A_y}{A_x + \theta_A E_{in}} $$

### calculate $E_{out}$
from BasicRunner import *

class Runner(BasicTxRunner):
    def __init__(self) -> None:
        super().__init__()

    def get_uni_v3_cur_tick(self):
        slot0 = self.get_uni_v3_slot0()
        return slot0[1]

    def run_01(self):
        # 240956//200 = 1204
        # 1204 >> 8 = 4
        cur_tick = self.get_uni_v3_cur_tick()
        index = (cur_tick//200)>>8
        bitmap_value = self.get_uni_v3_tick_bitmap_value(index)
        # tick_value = self.uni_v3.tick_bitmap(index)
        # print(tick_value)
        print(f"{bitmap_value:0256b}")
        pos = (cur_tick//200)%256
        print(f"{1<<pos:0256b}")

    def get_valid_ticks(self, index):
        bitmap_value = self.get_uni_v3_tick_bitmap_value(index)
        valid_ticks = []

        base_tick = index<<8

        for i in range(256):
            test_byte = 1<<i
            if bitmap_value & test_byte != 0:
                tick = (base_tick + i)*200
                valid_ticks.append(tick)

        return valid_ticks

    def run_02(self):
        # tick_info = self.get_uni_v3_tick_info(240600)
        valid_ticks = self.get_valid_ticks(4)
        for tick in valid_ticks:
            tick_info = self.get_uni_v3_tick_info(tick)
            [gross, net]= [tick_info[0], tick_info[1]]
            # print(f"tick: {tick}, ({gross},{net})")
            result = False
            if ((gross + net) == 0 )| ((gross - net) == 0):
                result = True

            print(f"[{tick}, {gross}, {net}, {result}]")

    # [237000, 1494217732916740105592978, 1494217732916740105592978, True]
    # [237200, 474263988605818822842519, 474263988605818822842519, True]
    # [238200, 1397830835357609705312628, 1397830835357609705312628, True]
    # [240600, 243372426883160345371157, 243372426883160345371157, True]
    # [240800, 369707920110159194101091, -369707920110159194101091, True]
    # [242600, 271304013383074897563477, -271304013383074897563477, True]
    # [243200, 201165671765013078239744, -201165671765013078239744, True]
    # [243400, 169557708208079764518320, -169557708208079764518320, True]
    # [244600, 38417944059114717433414, -38417944059114717433414, True]
    # [246000, 555754317389585464315108, -555754317389585464315108, True]
    def run_03(self):
        valid_ticks = self.get_valid_ticks(4)
        real_liquidity = self.get_uni_v3_liquidity()
        real_tick = self.get_uni_v3_cur_tick()
        # print(real_tick)

        # for i in range(valid_ticks)
        delta_liquidity = 0
        liquidity_list = []
        prev_liquidity = 0
        for i in range(len(valid_ticks)):
            check_tick = valid_ticks[i]
            tick_info = self.get_uni_v3_tick_info(check_tick)
            liquidity_net = tick_info[1]
            acc_liquidity = prev_liquidity + liquidity_net
            liquidity_item = [check_tick, acc_liquidity]
            liquidity_list.append(liquidity_item)
            prev_liquidity = acc_liquidity 

            if i < len(valid_ticks) - 1:
                if (valid_ticks[i] <= real_tick) & (real_tick < valid_ticks[i+1]):
                    delta_liquidity = real_liquidity - acc_liquidity 

        chart_data = []
        for i in range(len(liquidity_list)):
            start = liquidity_list[i][0]
            liquidity = liquidity_list[i][1] + delta_liquidity

            if i == len(liquidity_list)-1:
                end = start + 200
            else:
                next_start = liquidity_list[i+1][0]
                end = next_start

            # chart_item = [start, end, liquidity]
            # chart_item_a = [start, liquidity]
            # chart_item_b = [end, liquidity]
            # chart_list.append(chart_item_a)
            # chart_list.append(chart_item_b)
            chart_data.append([start, end, liquidity])

        for item in chart_data:
            print(f"[{item[0]}, {item[1]}, {item[2]//ETH}], ")

        # x_list = []
        # y_list = []
        # for item in chart_list:
        #     x_list.append(item[0])
        #     y_list.append(item[1])

        # print(x_list)
        # print(y_list)


if __name__ == "__main__":
    start_anvil()
    Runner().run_03()
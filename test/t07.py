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

class Runner2(BasicTxRunnerV2):
    def __init__(self, address) -> None:
        super().__init__()
        self.rlb_uni_v3 = UniswapV3(address)
        self.cur_liquidity = self.rlb_uni_v3.liquidity()
        self.cur_tick = self.rlb_uni_v3.slot0()[1]
        self.tick_spacing = self.rlb_uni_v3.tick_spacing()

    def run_01(self):
        cur_liquidity = self.rlb_uni_v3.liquidity()
        print(cur_liquidity)
        tick_spacing = self.rlb_uni_v3.tick_spacing()
        print(tick_spacing)

        cur_tick = self.rlb_uni_v3.slot0()[1]
        compressed = cur_tick // tick_spacing

        print(f"cur_tick: {cur_tick}, compresed: {compressed}")
        cur_tick_bitmap_index = compressed >> 8
        print(cur_tick_bitmap_index)
        bitmap_value = self.rlb_uni_v3.tick_bitmap(cur_tick_bitmap_index)
        print(f"{bitmap_value:0256b}")
        value_pos = compressed % 256
        print(f"{1<<value_pos:0256b}")

        liquidity_list = []
        base_compressed_index = cur_tick_bitmap_index << 8
        prev_liquidity = 0

        print("load tick info")
        acc_liquidity = prev_liquidity
        for i in range(256):
            print(f"\r{i*100/256:.2f}", end="")
            compressed_index = base_compressed_index + i
            tick_index = compressed_index * tick_spacing

            if i == 0:
                item = [tick_index, 0]
                liquidity_list.append(item)

            mask = 1<<i
            if bitmap_value & mask != 0:

                net_liquidity = self.rlb_uni_v3.ticks(tick_index)[1]
                acc_liquidity = prev_liquidity + net_liquidity
                item = [tick_index, acc_liquidity]
                liquidity_list.append(item)
                prev_liquidity = acc_liquidity

                print(f"[{tick_index:8}, {acc_liquidity//ETH}],")

            if i == 255:
                item = [tick_index, acc_liquidity]
                liquidity_list.append(item)


        delta_liquidity = 0
        for i in range(len(liquidity_list)):
            # tick_index = liquidity_list[i][0]
            if i < len(liquidity_list)-1:
                this_tick = liquidity_list[i][0]
                next_tick = liquidity_list[i+1][0]
                if (this_tick <= cur_tick) & (cur_tick < next_tick): 
                    this_liquidity = liquidity_list[i][1]
                    delta_liquidity = cur_liquidity - this_liquidity
                    print(f"delta_liquidity: {this_tick}, {delta_liquidity}, {cur_liquidity}, {this_liquidity}")
                    break


        chart_data = []
        for i in range(len(liquidity_list)):
            this_liquidity = liquidity_list[i][1]
            liquidity = this_liquidity + delta_liquidity
            start_index = liquidity_list[i][0]

            if i == (len(liquidity_list)-1):
                end_index = start_index + 256
            else:
                end_index = liquidity_list[i+1][0]

            item = [start_index, end_index, liquidity]
            print(f"[{start_index:8}, {end_index:8}, {liquidity//ETH}],")
            chart_data.append(item)

    def get_acc_liquidity_list(self):
        # cur_liquidity = self.rlb_uni_v3.liquidity()
        # tick_spacing = self.rlb_uni_v3.tick_spacing()
        # cur_tick = self.rlb_uni_v3.slot0()[1]
        compressed = self.cur_tick // self.tick_spacing
        cur_tick_bitmap_index = compressed >> 8
        bitmap_value = self.rlb_uni_v3.tick_bitmap(cur_tick_bitmap_index)

        liquidity_list = []
        base_compressed_index = cur_tick_bitmap_index << 8
        prev_liquidity = 0

        print("load tick info")
        for i in range(256):
            print(f"\r{i*100/256:.2f}", end="")
            compressed_index = base_compressed_index + i
            tick_index = compressed_index * self.tick_spacing 

            if i == 0:
                item = [tick_index, 0]
                liquidity_list.append(item)

            mask = 1<<i
            if bitmap_value & mask != 0:

                net_liquidity = self.rlb_uni_v3.ticks(tick_index)[1]
                acc_liquidity = prev_liquidity + net_liquidity
                item = [tick_index, acc_liquidity]
                liquidity_list.append(item)
                prev_liquidity = acc_liquidity

            if i == 255:
                item = [tick_index, acc_liquidity]
                liquidity_list.append(item)
        # print()

        delta_liquidity = 0
        for i in range(len(liquidity_list)):
            # tick_index = liquidity_list[i][0]
            if i < len(liquidity_list)-1:
                this_tick = liquidity_list[i][0]
                next_tick = liquidity_list[i+1][0]
                if (this_tick <= self.cur_tick) & (self.cur_tick < next_tick): 
                    this_liquidity = liquidity_list[i][1]
                    delta_liquidity = self.cur_liquidity - this_liquidity
                    break
        
        result_list = []
        for i in range(len(liquidity_list)):
            this_liquidity = liquidity_list[i][1]
            liquidity = this_liquidity + delta_liquidity
            start_index = liquidity_list[i][0]

            if i == (len(liquidity_list)-1):
                end_index = start_index + 256
            else:
                end_index = liquidity_list[i+1][0]

            item = [start_index, end_index, liquidity]
            print(f"[{start_index:8}, {end_index:8}, {liquidity//ETH}],")
            result_list.append(item)

        return result_list
    
    # [ -107520,  -105840, 379476],
    # [ -105840,  -105180, 380336],
    # [ -105180,  -104820, 380798],
    # [ -104820,  -104220, 382327],
    # [ -104220,  -104040, 391693],
    # [ -104040,  -103560, 392360],
    # [ -103560,  -103500, 406688],
    # [ -103500,  -103020, 412778],
    def run_02(self):
        print(self.cur_liquidity)
        liquidity_list = self.get_acc_liquidity_list()

        for raw_item in liquidity_list:
            [start, end, liquidity] = raw_item
            # liquidity = liquidity_list
            start_price = 1.0001**(start - self.cur_tick) * 100
            end_price = 1.0001**(end - self.cur_tick) * 100
            # item = [start_price, end_price, liquidity//ETH]
            print(f"[{start_price:3.2f}, {end_price:3.2f}, {liquidity//ETH}],")


RLB_UNI_V3 = "0x510100D5143e011Db24E2aa38abE85d73D5B2177"
USDC_UNI_V3 = "0x88e6A0c2dDD26FEEb64F039a2c41296FcB3f5640"
XRP_UNI_V3 = "0x663894588C6245Fe6FAC16713673471B2DaD4993"
RLB_USDT_V3 = "0x33676385160f9d8f03a0db2821029882f7c79e93"

if __name__ == "__main__":
    start_anvil(17589010)
    # Runner2(PEPE_UNI_V3).run_02()
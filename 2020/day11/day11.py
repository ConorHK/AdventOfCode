#!/usr/bin/env python3
from copy import deepcopy
from IPython.display import clear_output
import time

class PartOne:
    EMPTY_SEAT = 'L'
    FLOOR = '.'
    OCCUPIED_SEAT = '#'
    ADJACENT_POSITIONS =[
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    TOLERANCE = 4

    def __init__(self, seats):
        self.seats = seats
        self.ROW_LENGTH = len(seating_plan)
        self.COLUMN_LENGTH = len(seating_plan[0])

    def print(self):
        clear_output(wait=True)
        print('\n'.join("".join(seat) for seat in self.seats))

    def position_in_bounds(self, x, y):
        return x in range(self.ROW_LENGTH) and y in range(self.COLUMN_LENGTH)

    def adjacent_state(self, curr_seat_x, curr_seat_y):
        occupied = 0
        for left_right, above_below in self.ADJACENT_POSITIONS:
            adjacent_seat_x, adjacent_seat_y, within_range = self.get_adjacent_seat_pos(curr_seat_x, curr_seat_y, left_right, above_below)
            occupied += within_range and self.seats[adjacent_seat_x][adjacent_seat_y] == self.OCCUPIED_SEAT
        return occupied

    def get_adjacent_seat_pos(self, x,y, x_increment, y_increment):
            x, y = x + x_increment, y + y_increment
            within_range = self.position_in_bounds(x, y)
            return (x, y, within_range)

    def update(self):
        while True:
            prev_round = self.seats
            self.seats = self.evolve()
            self.print()
            if prev_round == self.seats:
                break
        return

    def evolve(self, tolerance=4):
        seat_copy = deepcopy(self.seats)
        for row in range(self.ROW_LENGTH):
            for column in range(self.COLUMN_LENGTH):
                num_adjacent = self.adjacent_state(row, column)
                curr_seat = self.seats[row][column]
                if curr_seat == self.EMPTY_SEAT and num_adjacent == 0:
                    seat_copy[row][column] = self.OCCUPIED_SEAT
                elif curr_seat == self.OCCUPIED_SEAT and num_adjacent >= self.TOLERANCE:
                    seat_copy[row][column] = self.EMPTY_SEAT
        return seat_copy

    def number_of_occupied_seats(self):
        return sum(list(s.count(self.OCCUPIED_SEAT) for s in self.seats))

class PartTwo(PartOne):
    TOLERANCE = 5
    def adjacent_state(self, curr_seat_x, curr_seat_y):
        occupied = 0
        for left_right, above_below in self.ADJACENT_POSITIONS:
            adjacent_seat_x, adjacent_seat_y, within_range = self.get_adjacent_seat_pos(curr_seat_x, curr_seat_y, left_right, above_below)
            occupied += within_range and self.seats[adjacent_seat_x][adjacent_seat_y] == self.OCCUPIED_SEAT
        return occupied

    def get_adjacent_seat_pos(self, x, y, x_increment, y_increment):
            x, y, _ = super().get_adjacent_seat_pos(x, y, x_increment, y_increment)
            while ((within_range:=self.position_in_bounds(x,y)) and (self.seats[x][y] == self.FLOOR)):
                x += x_increment
                y += y_increment
            return (x, y, within_range)

seating_plan = [list(seat.strip()) for seat in open('day11_input.txt').readlines()]

part_one = PartOne(seating_plan)
part_one.update()
print(f"Part one: {part_one.number_of_occupied_seats()}")

time.sleep(5)

part_two = PartTwo(seating_plan)
part_two.update()
print(f"Part two: {part_two.number_of_occupied_seats()}")

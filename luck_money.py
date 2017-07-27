import pygame
import random
class Main:
	def __init__(self):
		pygame.init();
		self.width = 800;
		self.height = 600;
		self.screen = pygame.display.set_mode((self.width, self.height), 0, 32);
		pygame.display.set_caption("luck_money");
		self.unit = pygame.image.load("res/unit.png");
		self.__bar_stride = 8;
		self.__gamers = [];
		self.__gamer_count = 100;
		for i in range(0, self.__gamer_count):
			self.__gamers.append(100);
	def __message_process(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit();

	def __play_game(self):
		idx_list = range(100);
		for idx in idx_list:
			self.__update_lucky_money(idx, idx_list);
		
	def __update_lucky_money(self, give_money_gamer_index, idx_list):
		lucky_money = 10;
		idx_list = range(100);
		random.shuffle(idx_list);

		average = money / gamer_count;
		r = random.random();
		min_value = 0.01;
		max_value = average * 2.0;
		val = max_value * r + min_value * (1 - r);

		v = self.__gamers[give_money_gamer_index] - val;
		if v < 0.0:
			self.__gamers[give_money_gamer_index] = 0.0;
		else:
			self.__gamers[give_money_gamer_index] = v;

		for idx in range(0, self.__gamer_count):
			if idx != give_money_gamer_index:
				self.__gamers[idx] = self.__gamers[idx] + val;

		rest_money = money - val;

		if rest_money < 0.0:
			rest_money = 0.0;

		return rest_money;

	def update(self):
		while True:
			self.__message_process();
			self.screen.fill((0, 0, 0));

			self.__draw_bar(400, 600, 300);
			self.__draw_bar(400 + self.__bar_stride, 600, 250);

			pygame.display.update();

	def __draw_bar(self, lb_x, lb_y, height):
		img = pygame.transform.scale(self.unit, (self.__bar_stride, height));
		x = lb_x;
		y = lb_y - height;
		self.screen.blit(img, (x, y));

if __name__ == "__main__":
	game = Main();
	game.update(); 
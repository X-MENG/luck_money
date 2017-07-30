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
		self.red_unit = pygame.image.load("res/red_unit.png");
		self.__bar_stride = 8;
		self.__lucky_money_value = 10;
		self.__run = True;
		self.__sort_it = False;
		self.__episode = 0;
		self.__money = 100;
		self.__init_game();
		self.__max_game_count = 100;
		self.__cur_game_count = 0;
		self.__game_result = [];
	def __init_game(self):
		self.__gamers = [];
		self.__gamer_count = 100;
		self.__give_money_gamer_index = 0;
		self.__show_result_state = 0;
		self.__game_reset = False;
		for i in range(0, self.__gamer_count):
			self.__gamers.append(self.__money);

	def __message_process(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit();
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.__run = not self.__run;
				elif event.key == pygame.K_s:
					self.__sort_it = not self.__sort_it;
				elif event.key == pygame.K_r:
					self.__init_game();
		
	def __update_game(self):
		if self.__gamers[self.__give_money_gamer_index] < self.__lucky_money_value:
			#print("gamer: %s - over!" % self.__give_money_gamer_index);
			return False;
		
		#print("giver before: %s - money = %s" % (self.__give_money_gamer_index, self.__gamers[self.__give_money_gamer_index]));
		self.__gamers[self.__give_money_gamer_index] -= self.__lucky_money_value;
		#print("giver after:  %s - money = %s" % (self.__give_money_gamer_index, self.__gamers[self.__give_money_gamer_index]));

		rest_money = self.__lucky_money_value;
		gamer_idx_list = [];
		for i in range(0, self.__gamer_count):
			gamer_idx_list.append(i);

		random.shuffle(gamer_idx_list);
		pass_gamer_count = 1;

		max_get_money_gamer_index = 0;
		max_get_money_value = -9999;

		for gamer_idx in gamer_idx_list:
			if gamer_idx != self.__give_money_gamer_index:
				#print("rest_money = %s" % rest_money);
				n = self.__gamer_count - pass_gamer_count;
				if n <= 0:
					break;
				#print("join gamer count: %s" % n);
				average = rest_money / n;
				#print("average_money = %s" % average);
				r = random.random();
				min_value = 0.01;
				max_value = average * 2.0;
				#max_value = rest_money * 0.5;
				val = max_value * r + min_value * (1 - r);
				#print("get_money = %s" % val);
				#print("receiver before: %s - money = %s" % (gamer_idx, self.__gamers[gamer_idx]));
				if rest_money - val < 0 or n == 1:
					self.__gamers[gamer_idx] += rest_money;
					val = rest_money;
					rest_money = 0.0;
					#print("receiver after: %s - money = %s" % (gamer_idx, self.__gamers[gamer_idx]));
					#print("finish!");
					break;
				else:
					rest_money = rest_money - val;
					self.__gamers[gamer_idx] += val;
					#print("receiver after: %s - money = %s" % (gamer_idx, self.__gamers[gamer_idx]));

				if val > max_get_money_value:
					max_get_money_value = val;
					max_get_money_gamer_index = gamer_idx;

				pass_gamer_count = pass_gamer_count + 1;

		self.__give_money_gamer_index = max_get_money_gamer_index;
		self.__episode += 1;

		return True;

	def update(self):
		while True:
			self.__message_process();
			self.screen.fill((0, 0, 0));

			if self.__run == True:
				#self.__run = False;
				#if self.__give_money_gamer_index >= self.__gamer_count:
				#	self.__give_money_gamer_index = 0;

				if self.__update_game() == False:
					if self.__show_result_state == 0:
					 	if self.__cur_game_count >= self.__max_game_count:
					 		win_count = 0;
					 		for g in self.__game_result:
					 			if g > 50:
					 				win_count += 1;
					 		print("win prob = %s" % (win_count / self.__max_game_count));
					 		self.__show_result_state = 2;
					 	else:
					 		self.__game_reset = True;

				#self.__give_money_gamer_index += 1;
			
			s = [];
			idx = 0;
			for v in self.__gamers:
				s.append((v, idx));
				idx += 1;

			if self.__sort_it == True:
				s.sort();

			px = 0;
			winner_count = 0;
			for val in s:
				if val[1] == self.__give_money_gamer_index:
					self.__draw_bar(px, 600, int(val[0]), self.red_unit);
				else:
					self.__draw_bar(px, 600, int(val[0]), self.unit);
				if val[0] > self.__money:
					winner_count += 1;

				px += self.__bar_stride;
			#print("winner_count ===== %s" % winner_count);

			pygame.draw.line(self.screen, (255, 0, 0), (0,500), (800,500), 1);

			pygame.display.update();

			pygame.display.set_caption("luck_money - " + str(self.__episode));

			if self.__game_reset == True:
				self.__game_result.append(winner_count);
				self.__init_game();
				self.__game_reset = False;
				print("winner_count = %s" % winner_count);
				self.__episode = 0;
				self.__cur_game_count += 1;
		
	def __draw_bar(self, lb_x, lb_y, height, img):
		img = pygame.transform.scale(img, (self.__bar_stride, height));
		x = lb_x;
		y = lb_y - height;
		self.screen.blit(img, (x, y));

if __name__ == "__main__":
	game = Main();
	game.update(); 
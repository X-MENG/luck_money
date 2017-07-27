import pygame

class Main:
	def __init__(self):
		pygame.init();
		self.width = 800;
		self.height = 600;
		self.screen = pygame.display.set_mode((self.width, self.height), 0, 32);
		pygame.display.set_caption("luck_money");
		self.unit = pygame.image.load("res/unit.png");
		self.__bar_stride = 8;
	def __message_process(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit();

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
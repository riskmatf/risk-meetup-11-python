from tqdm import trange, tqdm
from time import sleep

for i in trange(100):
	sleep(0.5)

pbar = tqdm(range(100), postfix='CUSTOM POSTFIX')

#postavljanje custom bar formata
bar_format='{desc}{bar} preostalo:{remaining}{postfix}'
pbar.bar_format = bar_format

for _ in range(100):
	pbar.update(1)
	pbar.set_description(f"{_}-ta iteracija")
	sleep(0.02)






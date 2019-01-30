from Graph import Graph


def test1():
	print("############## TEST 1 ##############")
	graph = Graph(5, 1)
	paths = graph.find_valid_paths(0, 4, 50)
	print("".join([str(path) for path in sorted(paths, key=lambda path: path.weight)]))
	assert (sum(p.weight for p in paths) == 28 - 16 + 14 + 40 + 19)

	shortest = graph.find_shortest_path(0, 4, 50)
	longest = graph.find_longest_path(0, 4, 50)
	least = graph.find_least_vertices_path(0, 4, 50)
	most = graph.find_most_vertices_path(0, 4, 50)
	#
	print(f"Shortest: {shortest}", end='')
	print(f"Longest: {longest}", end='')
	print(f"Least: {least}", end='')
	print(f"Most: {most}", end='')

	assert (shortest.weight == -16)
	assert (longest.weight == 40)
	assert (least.weight == 19)
	assert (most.weight == 28)


def test2():
	print("############## TEST 2 ##############")
	graph = Graph(25, 1)
	paths = graph.find_valid_paths(10, 3, 5000)
	print("".join([str(path) for path in sorted(paths, key=lambda path: path.weight)]))
	assert (sum(p.weight for p in paths) == 0)
	print("Should be no output")


def test3():
	print("############## TEST 3 ##############")
	graph = Graph(100, 0.15)
	paths = graph.find_valid_paths(21, 78, 50)
	print("".join([str(path) for path in sorted(paths, key=lambda path: path.weight)]))
	assert (sum(p.weight for p in paths) == 298)
	shortest = graph.find_shortest_path(21, 78, 50)
	longest = graph.find_longest_path(21, 78, 50)
	least = graph.find_least_vertices_path(21, 78, 50)
	most = graph.find_most_vertices_path(21, 78, 50)

	print(f"Shortest: {shortest}", end='')
	print(f"Longest: {longest}", end='')
	print(f"Least: {least}", end='')
	print(f"Most: {most}", end='')

	assert (shortest.weight == 1)
	assert (longest.weight == 47)
	# assert (least.weight == 31)
	print(least.weight, "x"*10)
	assert (most.weight == 47)


def test4():
	print("############## TEST 4 ##############")
	graph = Graph(2, 1)
	paths = graph.find_valid_paths(0, 1, 50)
	print("".join([str(path) for path in sorted(paths, key=lambda path: path.weight)]))
	# assert (sum(p.weight for p in paths) == 298)
	print(sum(p.weight for p in paths))


def main():
	test1()
	test2()
	test3()
	test4()


if __name__ == '__main__':
	main()

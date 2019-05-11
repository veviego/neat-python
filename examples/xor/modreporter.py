from __future__ import print_function
from neat.reporting import StdOutReporter
from neat.six_util import iteritems, iterkeys


'''
Compute Newman-Girvan modularity metric
'''
def NG_modularity(genome):
    nodes = [k for k, _ in genome.nodes.items()]
    # Add input nodes
    connections = [k for k, _ in genome.connections.items()]
    print(f"Nodes: {nodes}\nConnections: {str(connections)}")
    return 0


class ModReporter(StdOutReporter):
    def __init__(self, show_species_detail):
        super().__init__(show_species_detail)
        self.modularities = {}  # indexed by genome key

    def end_generation(self, config, population, species_set):
        super().end_generation(config, population, species_set)
        if self.show_species_detail:
            for genome_id, genome in list(iteritems(population)):
                self.modularities[genome_id] = NG_modularity(genome)
            print(f"config inputs: {config}")
            # print("Modularities: ", self.modularities)

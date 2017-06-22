import os
import fileinput

NnMdStructure={
  'Containers': ['Container_1.md', 'Container_1.md'],
  'Convolution_Layers': [],
  'Loss_Functions': [],
  'Distance_Functions': [],
  'Dropout_Layers': [],
  'Embedding_Layers': [],
  'Merge_Layers': [],
  'Functional_API': [],
  'Non-linear_Activations': [],
  'Normalization_Layers': [],
  'Pooling_Layers': [],
  'Recurrent_Layers': [],
  'Simple_Layers': [],
  'Utilities': [],
}
OptimMdStructure={
  'Metrics': [],
}


NnPath = 'docs/APIdocs/layers/nn'
OptimPath = 'docs/APIdocs/layers/optim/Metrics'
NnOutputPath = 'docs/APIdocs/layers/nn/Merged_md'
OptimOutPath = 'docs/APIdocs/layers/optim/Merged_md/Metrics.md'


'''
NN Layer part
'''
NNymlString='  - NN:\n'
# Check is file
for parents_md in NnMdStructure.keys():
  # First check wheter all the files exist
  for son_md in NnMdStructure[parents_md]:
    try:
      assert os.path.isfile(os.path.join(os.path.join(NnPath, parents_md), son_md))
    except:
      print('Error: '+son_md+' does not exist')

  # Concate them together
  with open(os.path.join(NnOutputPath, parents_md)+'.md', 'w+') as outfile:
    outfile.write('# '+parents_md.replace('_', ' ')+'\n')
    for son_md in NnMdStructure[parents_md]:
      with open(os.path.join(os.path.join(NnPath, parents_md), son_md)) as infile:
        outfile.write(infile.read())
    print('- '+parents_md.replace('_', ' ')+': '+NnOutputPath[5:]+'/'+parents_md+'.md')
    NNymlString = NNymlString + '    - '+parents_md.replace('_', ' ')+': '+NnOutputPath[5:] + '/'+parents_md+'.md\n'

#print NNymlString

'''
Optim Layer part
'''
# Check is file
for son_md in OptimMdStructure['Metrics']:
  try:
    assert os.path.isfile(os.path.join(OptimPath, son_md))
  except:
    print('Error: '+son_md+' does not exist')
  # Concate them together
with open(OptimOutPath, 'w+') as outfile:
  outfile.write('# Metrics\n')
  for son_md in OptimMdStructure['Metrics']:
    with open(os.path.join(OptimPath, son_md)) as infile:
      outfile.write(infile.read())
  print('- APIdocs/layers/optim/Merged_md/Metrics.md')
OptimymlString='  - Optim:\n'+'    - Metrics: APIdocs/layers/optim/Merged_md/Metrics.md\n'

#print OptimymlString

# Remove Old NN and Optim from file


# Write to yml file
for line in fileinput.FileInput('mkdocs.yml',inplace=1):
  if ('APIdocs/layers/') in line or ('- NN:' in line) or ('- Optim:' in line):
    pass
  else:
    print line,

for line in fileinput.FileInput('mkdocs.yml',inplace=1):
  if "Python API Docs" in line:
      line=line.replace(line,line+NNymlString+OptimymlString)
  print line,

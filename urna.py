import os, time

candidatos_deputado_federal = {
    '7777': {'nome': 'Adriana Almeida', 'partido': 'SOLIDARIEDADE', 'votos': 0},
    '1111': {'nome': 'Aguinaldo Ribeiro', 'partido': 'PP', 'votos': 0},
    '1222': {'nome': 'Airton Pires', 'partido': 'PDT', 'votos': 0},
    '1300': {'nome': 'Álex Andrade', 'partido': 'PT', 'votos': 0},
    '2277': {'nome': 'Alexandre do Sindicato', 'partido': 'PL', 'votos': 0},
    '1800': {'nome': 'Alexandre Fernandes', 'partido': 'REDE', 'votos': 0},
    '2200': {'nome': 'Alexandro Coco Seco', 'partido': 'PL', 'votos': 0},
    '1477': {'nome': 'Aline Grey', 'partido': 'MISSÃO', 'votos': 0},
    '2007': {'nome': 'Aline Markinna', 'partido': 'PODE', 'votos': 0},
    '1217': {'nome': 'Allana Rodrigues', 'partido': 'PDT', 'votos': 0},
    '2012': {'nome': 'Amanda Csi', 'partido': 'PODE', 'votos': 0},
    '3512': {'nome': 'Ana Zélia', 'partido': 'DEMOCRATA', 'votos': 0},
    '2233': {'nome': 'André Amaral Filho', 'partido': 'PL', 'votos': 0},
    '3007': {'nome': 'Andrea Araujo', 'partido': 'NOVO', 'votos': 0},
    '5050': {'nome': 'Andréa Miranda', 'partido': 'PSOL', 'votos': 0},
    '7713': {'nome': 'Betinho da Rs', 'partido': 'SOLIDARIEDADE', 'votos': 0},
    '1415': {'nome': 'Beto Lima', 'partido': 'MISSÃO', 'votos': 0},
    '1899': {'nome': 'Boca', 'partido': 'REDE', 'votos': 0},
    '2222': {'nome': 'Cabo Gilberto Silva', 'partido': 'PL', 'votos': 0},
    '2223': {'nome': 'Cantora Munique Marinho', 'partido': 'PL', 'votos': 0},
    '1000': {'nome': 'Capitã Rebeca', 'partido': 'REPUBLICANOS', 'votos': 0},
    '2255': {'nome': 'Carol Gomes', 'partido': 'PL', 'votos': 0},
    '1414': {'nome': 'Catarina Neves ', 'partido': 'MISSÃO', 'votos': 0},
    '3044': {'nome': 'Catarina Rocha', 'partido': 'NOVO', 'votos': 0},
    '1833': {'nome': 'Catier Ferreira ', 'partido': 'REDE', 'votos': 0},
    '1166': {'nome': 'Cicinha', 'partido': 'PP', 'votos': 0},
    '2010': {'nome': 'Ciloca Barrozo', 'partido': 'PODE', 'votos': 0},
    '2500': {'nome': 'Coronel Almeida', 'partido': 'PRD', 'votos': 0},
    '4001': {'nome': 'Cris Furtado', 'partido': 'PSB', 'votos': 0},
    '7020': {'nome': 'Cristiano Mateus', 'partido': 'AVANTE', 'votos': 0},
    '3520': {'nome': 'Cristina Acs', 'partido': 'DEMOCRATA', 'votos': 0},
    '7030': {'nome': 'Cristina de João Bodin', 'partido': 'AVANTE', 'votos': 0},
    '1818': {'nome': 'Cristina Guerreira', 'partido': 'REDE', 'votos': 0},
    '2266': {'nome': 'Daniel Conhece', 'partido': 'PL', 'votos': 0},
    '7080': {'nome': 'Daniel Trigueiro', 'partido': 'AVANTE', 'votos': 0},
    '7070': {'nome': 'Danilo Ilton', 'partido': 'AVANTE', 'votos': 0},
    '2288': {'nome': 'Deda Claudino', 'partido': 'PL', 'votos': 0},
    '3030': {'nome': 'Diego Braytnner', 'partido': 'NOVO', 'votos': 0},
    '3001': {'nome': 'Djaneide Almeida', 'partido': 'NOVO', 'votos': 0},
    '5540': {'nome': 'Doutor Jhony', 'partido': 'PSD', 'votos': 0},
    '3022': {'nome': 'Dr. Danillo Ramalho', 'partido': 'NOVO', 'votos': 0},
    '4055': {'nome': 'Dr. Levy da Habitação', 'partido': 'PSB', 'votos': 0},
    '4444': {'nome': 'Dr. Damião', 'partido': 'UNIÃO', 'votos': 0},
    '1112': {'nome': 'Dr. Emerson Panta', 'partido': 'PP', 'votos': 0},
    '3500': {'nome': 'Early', 'partido': 'DEMOCRATA', 'votos': 0},
    '5055': {'nome': 'Edinho Mendes', 'partido': 'PSOL', 'votos': 0},
    '1813': {'nome': 'Eduarda Almeida', 'partido': 'REDE', 'votos': 0},
    '1444': {'nome': 'Eduardo William', 'partido': 'MISSÃO', 'votos': 0},
    '2599': {'nome': 'Eli Mansur', 'partido': 'PRD', 'votos': 0},
    '1100': {'nome': 'Eliza', 'partido': 'PP', 'votos': 0},
    '3003': {'nome': 'Emerson Wallace', 'partido': 'NOVO', 'votos': 0},
    '1333': {'nome': 'Mary Priscila', 'partido': 'PT', 'votos': 0},
    '1234': {'nome': 'Erika Von Sohsten', 'partido': 'PDT', 'votos': 0},
    '4040': {'nome': 'Fábio Tyrone', 'partido': 'PSB', 'votos': 0},
    '1400': {'nome': 'Francisco Mendonça', 'partido': 'MISSÃO', 'votos': 0},
    '2722': {'nome': 'Freitas', 'partido': 'DC', 'votos': 0},
    '1303': {'nome': 'Gabi Benvenutty', 'partido': 'PT', 'votos': 0},
    '7796': {'nome': 'Genilson Lucenyah', 'partido': 'SOLIDARIEDADE', 'votos': 0},
    '2211': {'nome': 'George Morais', 'partido': 'PL', 'votos': 0},
    '2212': {'nome': 'Gerana Gouveia', 'partido': 'PL', 'votos': 0},
    '7710': {'nome': 'Gerlane Freitas', 'partido': 'SOLIDARIEDADE', 'votos': 0},
    '5512': {'nome': 'Germana Wanderley', 'partido': 'PSD', 'votos': 0},
    '6565': {'nome': 'Gervásio Maia', 'partido': 'PCDOB', 'votos': 0},
    '1245': {'nome': 'Gilson Roberto (Ovão)', 'partido': 'PDT', 'votos': 0},
    '1123': {'nome': 'Guga Pet', 'partido': 'PP', 'votos': 0},
    '5508': {'nome': 'Helena Holanda', 'partido': 'PSD', 'votos': 0},
    '3055': {'nome': 'Henrique Queiroz', 'partido': 'NOVO', 'votos': 0},
    '2711': {'nome': 'Herick', 'partido': 'DC', 'votos': 0},
    '1144': {'nome': 'Hermerson Caminhoneiro', 'partido': 'PP', 'votos': 0},
    '1011': {'nome': 'Hugo', 'partido': 'REPUBLICANOS', 'votos': 0},
    '1211': {'nome': 'Inaldo Andrade', 'partido': 'PDT', 'votos': 0},
    '8080': {'nome': 'Isabele do Correnteza', 'partido': 'UP', 'votos': 0},
    '2055': {'nome': 'Jacó Maciel', 'partido': 'PODE', 'votos': 0},
    '4045': {'nome': 'Jailma Carvalho', 'partido': 'PSB', 'votos': 0},
    '3535': {'nome': 'Jandir Ferraz', 'partido': 'DEMOCRATA', 'votos': 0},
    '1020': {'nome': 'Janny Milanes', 'partido': 'REPUBLICANOS', 'votos': 0},
    '5550': {'nome': 'João dos Santos', 'partido': 'PSD', 'votos': 0},
    '8000': {'nome': 'Jonas Souza', 'partido': 'UP', 'votos': 0},
    '5507': {'nome': 'Júlia Venerando', 'partido': 'PSD', 'votos': 0},
    '1177': {'nome': 'Julian Lemos', 'partido': 'PP', 'votos': 0},
    '1212': {'nome': 'Juliana Almeida', 'partido': 'PDT', 'votos': 0},
    '5510': {'nome': 'Jullyana Ribeiro', 'partido': 'PSD', 'votos': 0},
    '3077': {'nome': 'Junior do Trem', 'partido': 'NOVO', 'votos': 0},
    '2777': {'nome': 'Kel Souza', 'partido': 'DC', 'votos': 0},
    '2767': {'nome': 'Krisna Gopal', 'partido': 'DC', 'votos': 0},
    '5556': {'nome': 'Lana Dantas', 'partido': 'PSD', 'votos': 0},
    '2900': {'nome': 'Latifi Abou Haikal', 'partido': 'PCO', 'votos': 0},
    '2020': {'nome': 'Léo Gadelha', 'partido': 'PODE', 'votos': 0},
    '4013': {'nome': 'Lídia Moura', 'partido': 'PSB', 'votos': 0},
    '1483': {'nome': 'Luan Brasiliano', 'partido': 'MISSÃO', 'votos': 0},
    '3066': {'nome': 'Lucenildo Branco', 'partido': 'NOVO', 'votos': 0},
    '1345': {'nome': 'Luiz Couto', 'partido': 'PT', 'votos': 0},
    '3347': {'nome': 'Lula da Tapioca', 'partido': 'MOBILIZA', 'votos': 0},
    '3311': {'nome': 'Lumitânia Dias', 'partido': 'MOBILIZA', 'votos': 0},
    '3577': {'nome': 'Mãe Goretti', 'partido': 'DEMOCRATA', 'votos': 0},
    '1066': {'nome': 'Maísa Cartaxo', 'partido': 'REPUBLICANOS', 'votos': 0},
    '1819': {'nome': 'Marcela Kelly', 'partido': 'REDE', 'votos': 0},
    '4343': {'nome': 'Marcella Viana', 'partido': 'PV', 'votos': 0},
    '1210': {'nome': 'Márcio Lins', 'partido': 'PDT', 'votos': 0},
    '3333': {'nome': 'Marcos Oliveira', 'partido': 'MOBILIZA', 'votos': 0},
    '3313': {'nome': 'Marilene Alves', 'partido': 'MOBILIZA', 'votos': 0},
    '4422': {'nome': 'Marília Dantas', 'partido': 'UNIÃO', 'votos': 0},
    '1236': {'nome': 'Mazureik Rodrigues', 'partido': 'PDT', 'votos': 0},
    '5555': {'nome': 'Mersinho Lucena', 'partido': 'PSD', 'votos': 0},
    '2077': {'nome': 'Miguel Pimenta', 'partido': 'PODE', 'votos': 0},
    '7090': {'nome': 'Missinho do Bode', 'partido': 'AVANTE', 'votos': 0},
    '3088': {'nome': 'Missionária Ivone do Hu', 'partido': 'NOVO', 'votos': 0},
    '1215': {'nome': 'Moca Medeiros', 'partido': 'PDT', 'votos': 0},
    '2780': {'nome': 'Monik Evellyn', 'partido': 'DC', 'votos': 0},
    '1044': {'nome': 'Murilo Galdino', 'partido': 'REPUBLICANOS', 'votos': 0},
    '2202': {'nome': 'Nágila Santana', 'partido': 'PL', 'votos': 0},
    '7010': {'nome': 'Neide Bicuda', 'partido': 'AVANTE', 'votos': 0},
    '2022': {'nome': 'Nelson Gomes', 'partido': 'PODE', 'votos': 0},
    '3511': {'nome': 'Nêm dos Óculos', 'partido': 'DEMOCRATA', 'votos': 0},
    '5515': {'nome': 'Netto Lima', 'partido': 'PSD', 'votos': 0},
    '3012': {'nome': 'Nildo Terra Boa', 'partido': 'NOVO', 'votos': 0},
    '1045': {'nome': 'Nilson Lacerda', 'partido': 'REPUBLICANOS', 'votos': 0},
    '7788': {'nome': 'Nilton Maia da Shalon', 'partido': 'SOLIDARIEDADE', 'votos': 0},
    '3555': {'nome': 'Nininho Mangabeira', 'partido': 'DEMOCRATA', 'votos': 0},
    '3310': {'nome': 'O Profeta Ivanildo', 'partido': 'MOBILIZA', 'votos': 0},
    '3510': {'nome': 'Pastor Robson', 'partido': 'DEMOCRATA', 'votos': 0},
    '2507': {'nome': 'Patrícia Berger', 'partido': 'PRD', 'votos': 0},
    '7711': {'nome': 'Patrícia Mota', 'partido': 'SOLIDARIEDADE', 'votos': 0},
    '1311': {'nome': 'Pedro Matias', 'partido': 'PT', 'votos': 0},
    '6500': {'nome': 'Percival', 'partido': 'PCDOB', 'votos': 0},
    '1088': {'nome': 'Policial Caio', 'partido': 'REPUBLICANOS', 'votos': 0},
    '7733': {'nome': 'Polly do Adota', 'partido': 'SOLIDARIEDADE', 'votos': 0},
    '1133': {'nome': 'Pollyanna', 'partido': 'PP', 'votos': 0},
    '5511': {'nome': 'Leila Fonseca', 'partido': 'PSD', 'votos': 0},
    '4015': {'nome': 'Rachel Maroja', 'partido': 'PSB', 'votos': 0},
    '3522': {'nome': 'Raimunda', 'partido': 'DEMOCRATA', 'votos': 0},
    '1015': {'nome': 'Raniery Paulino', 'partido': 'REPUBLICANOS', 'votos': 0},
    '5533': {'nome': 'Raoni Mendes', 'partido': 'PSD', 'votos': 0},
    '2555': {'nome': 'Ray Alencar', 'partido': 'PRD', 'votos': 0},
    '1001': {'nome': 'Renan da Resenha', 'partido': 'REPUBLICANOS', 'votos': 0},
    '4022': {'nome': 'Carlos Santos', 'partido': 'PSB', 'votos': 0},
    '1122': {'nome': 'Ricardo Barbosa', 'partido': 'PP', 'votos': 0},
    '1313': {'nome': 'Ricardo Coutinho', 'partido': 'PT', 'votos': 0},
    '4004': {'nome': 'Roberto Burity', 'partido': 'PSB', 'votos': 0},
    '7050': {'nome': 'Rodolfo Duarte', 'partido': 'AVANTE', 'votos': 0},
    '3000': {'nome': 'Rodrigo Lima', 'partido': 'NOVO', 'votos': 0},
    '2026': {'nome': 'Romero Rodrigues', 'partido': 'PODE', 'votos': 0},
    '6555': {'nome': 'Rosi Cruz', 'partido': 'PCDOB', 'votos': 0},
    '2030': {'nome': 'Ruy Carneiro', 'partido': 'PODE', 'votos': 0},
    '2710': {'nome': 'Samara Stefane', 'partido': 'DC', 'votos': 0},
    '5566': {'nome': 'Samuka', 'partido': 'PSD', 'votos': 0},
    '2011': {'nome': 'Sandra Marrocos', 'partido': 'PODE', 'votos': 0},
    '2755': {'nome': 'Sandro de Santa Rita', 'partido': 'DC', 'votos': 0},
    '2033': {'nome': 'Sara Cabral', 'partido': 'PODE', 'votos': 0},
    '1822': {'nome': 'Sargento Aglair', 'partido': 'REDE', 'votos': 0},
    '7040': {'nome': 'Sargento Etivaldo', 'partido': 'AVANTE', 'votos': 0},
    '4011': {'nome': 'Sargento Helmut', 'partido': 'PSB', 'votos': 0},
    '1267': {'nome': 'Sargento Karla', 'partido': 'PDT', 'votos': 0},
    '1240': {'nome': 'Sargento Lee', 'partido': 'PDT', 'votos': 0},
    '4050': {'nome': 'Sargento Wellington Cobra', 'partido': 'PSB', 'votos': 0},
    '1310': {'nome': 'Saulo Dantas', 'partido': 'PT', 'votos': 0},
    '3300': {'nome': 'Sergio do Real Preço', 'partido': 'MOBILIZA', 'votos': 0},
    '2727': {'nome': 'Sérgio Gama', 'partido': 'DC', 'votos': 0},
    '4410': {'nome': 'Sergio Rafael', 'partido': 'UNIÃO', 'votos': 0},
    '1022': {'nome': 'Silvia Benjamin', 'partido': 'REPUBLICANOS', 'votos': 0},
    '2000': {'nome': 'Silvia da Pesca', 'partido': 'PODE', 'votos': 0},
    '2512': {'nome': 'Silvio Soares', 'partido': 'PRD', 'votos': 0},
    '5000': {'nome': 'Sousa Neto', 'partido': 'PSOL', 'votos': 0},
    '2700': {'nome': 'Steffenie Jessica', 'partido': 'DC', 'votos': 0},
    '1107': {'nome': 'Tarcísio Jardim', 'partido': 'PP', 'votos': 0},
    '5013': {'nome': 'Taty Paraíba Feminina', 'partido': 'PSOL', 'votos': 0},
    '3033': {'nome': 'Tc Edilson Bernardo', 'partido': 'NOVO', 'votos': 0},
    '1200': {'nome': 'Tenente Jair', 'partido': 'PDT', 'votos': 0},
    '2269': {'nome': 'Tia Mila', 'partido': 'PL', 'votos': 0},
    '1033': {'nome': 'Tião Gomes', 'partido': 'REPUBLICANOS', 'votos': 0},
    '1856': {'nome': 'Tota dos Animais', 'partido': 'REDE', 'votos': 0},
    '7724': {'nome': 'Trajano', 'partido': 'SOLIDARIEDADE', 'votos': 0},
    '2929': {'nome': 'Val Alves', 'partido': 'PCO', 'votos': 0},
    '7011': {'nome': 'Valdecir Junior', 'partido': 'AVANTE', 'votos': 0},
    '1077': {'nome': 'Valdir Trindade', 'partido': 'REPUBLICANOS', 'votos': 0},
    '1811': {'nome': 'Walkíria Lins', 'partido': 'REDE', 'votos': 0},
    '5522': {'nome': 'Wellington Roberto', 'partido': 'PSD', 'votos': 0},
    '1213': {'nome': 'Wellington Silva Sousa', 'partido': 'PDT', 'votos': 0},
    '1010': {'nome': 'Wilson Santiago', 'partido': 'REPUBLICANOS', 'votos': 0},
    '7060': {'nome': 'Zé Marcos', 'partido': 'AVANTE', 'votos': 0},
    '4000': {'nome': 'Zezinho Botafogo', 'partido': 'PSB', 'votos': 0},
}

candidatos_deputado_estadual = {
    '10444': {'nome': 'Adriano Galdino', 'partido': 'REPUBLICANOS', 'votos': 0},
    '22622': {'nome': 'Alan de Bastos', 'partido': 'PL', 'votos': 0},
    '40040': {'nome': 'Aldenora Bezerra', 'partido': 'PSB', 'votos': 0},
    '22077': {'nome': 'Alexandre Rei dos Terrenos', 'partido': 'PL', 'votos': 0},
    '13206': {'nome': 'Ana Araújo', 'partido': 'PT', 'votos': 0},
    '15678': {'nome': 'Ana Cláudia', 'partido': 'MDB', 'votos': 0},
    '43147': {'nome': 'Anderson Monteiro', 'partido': 'PV', 'votos': 0},
    '22555': {'nome': 'André Gomes', 'partido': 'PL', 'votos': 0},
    '11999': {'nome': 'André Matias', 'partido': 'PP', 'votos': 0},
    '18691': {'nome': 'Anely Mônica', 'partido': 'REDE', 'votos': 0},
    '40013': {'nome': 'Anísio Maia', 'partido': 'PSB', 'votos': 0},
    '12192': {'nome': 'Barbosa de Mandacaru', 'partido': 'PDT', 'votos': 0},
    '11177': {'nome': 'Bispo José Luiz', 'partido': 'PP', 'votos': 0},
    '11113': {'nome': 'Bosco Carneiro', 'partido': 'PP', 'votos': 0},
    '10888': {'nome': 'Branco Mendes', 'partido': 'REPUBLICANOS', 'votos': 0},
    '43111': {'nome': 'Bruna Morais', 'partido': 'PV', 'votos': 0},
    '15222': {'nome': 'Caio Roberto', 'partido': 'MDB', 'votos': 0},
    '15111': {'nome': 'Camila Toscano', 'partido': 'MDB', 'votos': 0},
    '22007': {'nome': 'Capitã Aline', 'partido': 'PL', 'votos': 0},
    '10193': {'nome': 'Capitão Maradona', 'partido': 'REPUBLICANOS', 'votos': 0},
    '12444': {'nome': 'Capitão Pereira', 'partido': 'PDT', 'votos': 0},
    '22777': {'nome': 'Carlão Pelo Bem', 'partido': 'PL', 'votos': 0},
    '15650': {'nome': 'Carlinhos de Nias', 'partido': 'MDB', 'votos': 0},
    '40640': {'nome': 'Carlos Renato', 'partido': 'PSB', 'votos': 0},
    '11456': {'nome': 'Célia Alves', 'partido': 'PP', 'votos': 0},
    '43789': {'nome': 'Chió', 'partido': 'PV', 'votos': 0},
    '18800': {'nome': 'Cícero Simplício', 'partido': 'REDE', 'votos': 0},
    '10144': {'nome': 'Cicinho Lima', 'partido': 'REPUBLICANOS', 'votos': 0},
    '13400': {'nome': 'Cida Ramos', 'partido': 'PT', 'votos': 0},
    '22444': {'nome': 'Cilinha', 'partido': 'PL', 'votos': 0},
    '22878': {'nome': 'Cláudio O Servente de Obras', 'partido': 'PL', 'votos': 0},
    '22088': {'nome': 'Cloves Malvinas', 'partido': 'PL', 'votos': 0},
    '10404': {'nome': 'Coronel Lucas', 'partido': 'REPUBLICANOS', 'votos': 0},
    '10190': {'nome': 'Coronel Sergio', 'partido': 'REPUBLICANOS', 'votos': 0},
    '22789': {'nome': 'Coronel Sobreira', 'partido': 'PL', 'votos': 0},
    '11200': {'nome': 'Dane Alencar', 'partido': 'PP', 'votos': 0},
    '40444': {'nome': 'Daniel da Saúde', 'partido': 'PSB', 'votos': 0},
    '44111': {'nome': 'Daniel Gomes', 'partido': 'UNIÃO', 'votos': 0},
    '22822': {'nome': 'Daniel Sobrinho', 'partido': 'PL', 'votos': 0},
    '10456': {'nome': 'Danielle do Vale', 'partido': 'REPUBLICANOS', 'votos': 0},
    '12000': {'nome': 'Denise Ribeiro', 'partido': 'PDT', 'votos': 0},
    '22422': {'nome': 'Deputa Mané Buchada', 'partido': 'PL', 'votos': 0},
    '11000': {'nome': 'Diego Tavares', 'partido': 'PP', 'votos': 0},
    '15789': {'nome': 'Dinho', 'partido': 'MDB', 'votos': 0},
    '40400': {'nome': 'Diva', 'partido': 'PSB', 'votos': 0},
    '12321': {'nome': 'Dr. André Lima', 'partido': 'PDT', 'votos': 0},
    '43000': {'nome': 'Dr. Athaide', 'partido': 'PV', 'votos': 0},
    '43777': {'nome': 'Dr. Bruno Deriu', 'partido': 'PV', 'votos': 0},
    '22522': {'nome': 'Dr. Evandro Trindade', 'partido': 'PL', 'votos': 0},
    '10777': {'nome': 'Dr. Jarques', 'partido': 'REPUBLICANOS', 'votos': 0},
    '13123': {'nome': 'Dr. Jefferson', 'partido': 'PT', 'votos': 0},
    '15155': {'nome': 'Dr. Pet', 'partido': 'MDB', 'votos': 0},
    '65123': {'nome': 'Dr. Romualdo', 'partido': 'PCDOB', 'votos': 0},
    '40345': {'nome': 'Dra Flavina Feliciano', 'partido': 'PSB', 'votos': 0},
    '11111': {'nome': 'Dra Jane Panta', 'partido': 'PP', 'votos': 0},
    '11007': {'nome': 'Dudu Soares', 'partido': 'PP', 'votos': 0},
    '40777': {'nome': 'Eduardo Brito', 'partido': 'PSB', 'votos': 0},
    '11333': {'nome': 'Eduardo Carneiro', 'partido': 'PP', 'votos': 0},
    '18456': {'nome': 'Eliezer Benício', 'partido': 'REDE', 'votos': 0},
    '15150': {'nome': 'Raquel Paula', 'partido': 'MDB', 'votos': 0},
    '10192': {'nome': 'Rayra Beserra', 'partido': 'REPUBLICANOS', 'votos': 0},
    '22400': {'nome': 'Joab', 'partido': 'PL', 'votos': 0},
    '12247': {'nome': 'Evilliane Lins', 'partido': 'PDT', 'votos': 0},
    '22500': {'nome': 'Fabiano Soares', 'partido': 'PL', 'votos': 0},
    '22000': {'nome': 'Fábio Lopes', 'partido': 'PL', 'votos': 0},
    '15555': {'nome': 'Fábio Ramalho', 'partido': 'MDB', 'votos': 0},
    '11555': {'nome': 'Fabiola Rezende', 'partido': 'PP', 'votos': 0},
    '10222': {'nome': 'Felipe Coutinho', 'partido': 'REPUBLICANOS', 'votos': 0},
    '15999': {'nome': 'Felipe Leitão', 'partido': 'MDB', 'votos': 0},
    '44444': {'nome': 'Fernanda Alvino', 'partido': 'UNIÃO', 'votos': 0},
    '13333': {'nome': 'Flávio Brasileiro', 'partido': 'PT', 'votos': 0},
    '11222': {'nome': 'Galego Souza', 'partido': 'PP', 'votos': 0},
    '40196': {'nome': 'Gerlane', 'partido': 'PSB', 'votos': 0},
    '22333': {'nome': 'Geska de Laurinho', 'partido': 'PL', 'votos': 0},
    '44555': {'nome': 'Gilbertinho', 'partido': 'UNIÃO', 'votos': 0},
    '18789': {'nome': 'Gilberto Calado', 'partido': 'REDE', 'votos': 0},
    '50555': {'nome': 'Gilson Dantas (Papaléguas)', 'partido': 'PSOL', 'votos': 0},
    '15123': {'nome': 'Hervazio Bezerra', 'partido': 'MDB', 'votos': 0},
    '65555': {'nome': 'Inácio Falcão', 'partido': 'PCDOB', 'votos': 0},
    '15115': {'nome': 'Jaci Guimarães', 'partido': 'MDB', 'votos': 0},
    '11234': {'nome': 'Jader Pimentel Filho', 'partido': 'PP', 'votos': 0},
    '40999': {'nome': 'Janine Oliveira', 'partido': 'PSB', 'votos': 0},
    '13100': {'nome': 'Jânio Pereira', 'partido': 'PT', 'votos': 0},
    '40555': {'nome': 'Jeane Oliveira', 'partido': 'PSB', 'votos': 0},
    '65000': {'nome': 'Jô Oliveira', 'partido': 'PCDOB', 'votos': 0},
    '15777': {'nome': 'Joallison Santos', 'partido': 'MDB', 'votos': 0},
    '11888': {'nome': 'João Batista de Bayeux', 'partido': 'PP', 'votos': 0},
    '11611': {'nome': 'João Gonçalves', 'partido': 'PP', 'votos': 0},
    '11369': {'nome': 'João Paulo Segundo', 'partido': 'PP', 'votos': 0},
    '12333': {'nome': 'Joaquim Morais', 'partido': 'PDT', 'votos': 0},
    '12567': {'nome': 'Jorge Maia', 'partido': 'PDT', 'votos': 0},
    '40401': {'nome': 'Jose Pereira', 'partido': 'PSB', 'votos': 0},
    '80123': {'nome': 'Jozivan Antero', 'partido': 'UP', 'votos': 0},
    '12123': {'nome': 'Junio Leandro', 'partido': 'PDT', 'votos': 0},
    '11777': {'nome': 'Júnior Araújo', 'partido': 'PP', 'votos': 0},
    '10123': {'nome': 'Jutay Meneses', 'partido': 'REPUBLICANOS', 'votos': 0},
    '50333': {'nome': 'Kaline', 'partido': 'PSOL', 'votos': 0},
    '11500': {'nome': 'Kelly do Botafogo', 'partido': 'PP', 'votos': 0},
    '40111': {'nome': 'Klécida Rodrigues', 'partido': 'PSB', 'votos': 0},
    '43333': {'nome': 'Lafa Gadelha', 'partido': 'PV', 'votos': 0},
    '22287': {'nome': 'Lampião Gaúcho', 'partido': 'PL', 'votos': 0},
    '15000': {'nome': 'Larúcia', 'partido': 'MDB', 'votos': 0},
    '15666': {'nome': 'Lena do Paraíba', 'partido': 'MDB', 'votos': 0},
    '10999': {'nome': 'Leonice Lopes', 'partido': 'REPUBLICANOS', 'votos': 0},
    '11123': {'nome': 'Lindolfo Pires', 'partido': 'PP', 'votos': 0},
    '11211': {'nome': 'Lorena', 'partido': 'PP', 'votos': 0},
    '11444': {'nome': 'Lucas Caçula', 'partido': 'PP', 'votos': 0},
    '11022': {'nome': 'Lucas Lucena', 'partido': 'PP', 'votos': 0},
    '40333': {'nome': 'Lucca Nuto', 'partido': 'PSB', 'votos': 0},
    '10660': {'nome': 'Luciano Cartaxo', 'partido': 'REPUBLICANOS', 'votos': 0},
    '43027': {'nome': 'Luciene Farias', 'partido': 'PV', 'votos': 0},
    '44144': {'nome': 'Madá', 'partido': 'UNIÃO', 'votos': 0},
    '15112': {'nome': 'Madalena Cabeleireira', 'partido': 'MDB', 'votos': 0},
    '11190': {'nome': 'Major Fernando', 'partido': 'PP', 'votos': 0},
    '43123': {'nome': 'Manoel Ludgério', 'partido': 'PV', 'votos': 0},
    '15888': {'nome': 'Manu de Souza', 'partido': 'MDB', 'votos': 0},
    '11138': {'nome': 'Marcia da Salada', 'partido': 'PP', 'votos': 0},
    '10234': {'nome': 'Marcio Roberto', 'partido': 'REPUBLICANOS', 'votos': 0},
    '43555': {'nome': 'Marcos Eron', 'partido': 'PV', 'votos': 0},
    '13000': {'nome': 'Marcos Henriques', 'partido': 'PT', 'votos': 0},
    '44123': {'nome': 'Maria Porto', 'partido': 'UNIÃO', 'votos': 0},
    '40789': {'nome': 'Marinaldo Cardoso', 'partido': 'PSB', 'votos': 0},
    '12456': {'nome': 'Marlangela', 'partido': 'PDT', 'votos': 0},
    '22321': {'nome': 'Mary', 'partido': 'PL', 'votos': 0},
    '18888': {'nome': 'Max Júnior', 'partido': 'REDE', 'votos': 0},
    '22888': {'nome': 'Melca Farias', 'partido': 'PL', 'votos': 0},
    '22100': {'nome': 'Merinha da Casa de Apoio', 'partido': 'PL', 'votos': 0},
    '11011': {'nome': 'Michel Henrique', 'partido': 'PP', 'votos': 0},
    '22345': {'nome': 'Michely Farina', 'partido': 'PL', 'votos': 0},
    '12108': {'nome': 'Monica Rodrigues', 'partido': 'PDT', 'votos': 0},
    '12223': {'nome': 'Morena', 'partido': 'PDT', 'votos': 0},
    '10000': {'nome': 'Natália Rodrigues', 'partido': 'REPUBLICANOS', 'votos': 0},
    '44333': {'nome': 'Nathalya Fernanda', 'partido': 'UNIÃO', 'votos': 0},
    '50123': {'nome': 'Neidinha', 'partido': 'PSOL', 'votos': 0},
    '40123': {'nome': 'Nelinho Costa', 'partido': 'PSB', 'votos': 0},
    '18777': {'nome': 'Nice Costa', 'partido': 'REDE', 'votos': 0},
    '40456': {'nome': 'Nil Mendes', 'partido': 'PSB', 'votos': 0},
    '22222': {'nome': 'Nilvan Ferreira', 'partido': 'PL', 'votos': 0},
    '10180': {'nome': 'Nobinho Almeida', 'partido': 'REPUBLICANOS', 'votos': 0},
    '13213': {'nome': 'Noca Ribeiro', 'partido': 'PT', 'votos': 0},
    '10111': {'nome': 'Olívia Motta', 'partido': 'REPUBLICANOS', 'votos': 0},
    '15669': {'nome': 'Osvaldo Santos', 'partido': 'MDB', 'votos': 0},
    '11083': {'nome': 'Paulo Ferreira', 'partido': 'PP', 'votos': 0},
    '15919': {'nome': 'Poca Cabeleireiro', 'partido': 'MDB', 'votos': 0},
    '15022': {'nome': 'Pr. Isaac Venerando', 'partido': 'MDB', 'votos': 0},
    '80800': {'nome': 'Prof. Cleber', 'partido': 'UP', 'votos': 0},
    '15321': {'nome': 'Prof. Hosana Carneiro', 'partido': 'MDB', 'votos': 0},
    '13130': {'nome': 'Prof. Stenio Soares', 'partido': 'PT', 'votos': 0},
    '22770': {'nome': 'Professor Arlison', 'partido': 'PL', 'votos': 0},
    '13613': {'nome': 'Professor Edileudo Lucena', 'partido': 'PT', 'votos': 0},
    '15300': {'nome': 'Professor Francisco', 'partido': 'MDB', 'votos': 0},
    '22922': {'nome': 'Professor Josias Mendes', 'partido': 'PL', 'votos': 0},
    '15015': {'nome': 'Professor Roni Andrade', 'partido': 'MDB', 'votos': 0},
    '10789': {'nome': 'Professora Ivonete', 'partido': 'REPUBLICANOS', 'votos': 0},
    '12678': {'nome': 'Professora Kalina', 'partido': 'PDT', 'votos': 0},
    '50111': {'nome': 'Raimundo Agente de Saúde', 'partido': 'PSOL', 'votos': 0},
    '22022': {'nome': 'Raquel França', 'partido': 'PL', 'votos': 0},
    '18000': {'nome': 'Ricardo Lucena', 'partido': 'REDE', 'votos': 0},
    '15200': {'nome': 'Roberto Lima', 'partido': 'MDB', 'votos': 0},
    '11400': {'nome': 'Rosália Lucas', 'partido': 'PP', 'votos': 0},
    '13110': {'nome': 'Rosely Louzada', 'partido': 'PT', 'votos': 0},
    '11321': {'nome': 'Ruan Martins', 'partido': 'PP', 'votos': 0},
    '22001': {'nome': 'Samara Suassuna', 'partido': 'PL', 'votos': 0},
    '22122': {'nome': 'Sammara Aguiar Sammy', 'partido': 'PL', 'votos': 0},
    '12190': {'nome': 'Sargento Barlavento', 'partido': 'PDT', 'votos': 0},
    '22191': {'nome': 'Sargento Cleber', 'partido': 'PL', 'votos': 0},
    '18188': {'nome': 'Sargento Ivaldo Garrincha', 'partido': 'REDE', 'votos': 0},
    '22999': {'nome': 'Sargento Neto', 'partido': 'PL', 'votos': 0},
    '15190': {'nome': 'Sargento Rui', 'partido': 'MDB', 'votos': 0},
    '12111': {'nome': 'Sargento Sérgio Araujo', 'partido': 'PDT', 'votos': 0},
    '12100': {'nome': 'Sávio Salvador', 'partido': 'PDT', 'votos': 0},
    '22456': {'nome': 'Segundo Domiciano', 'partido': 'PL', 'votos': 0},
    '40234': {'nome': 'Sibelle Barros', 'partido': 'PSB', 'votos': 0},
    '15192': {'nome': 'Subtenente Crispim', 'partido': 'MDB', 'votos': 0},
    '13111': {'nome': 'Suelma Tavares', 'partido': 'PT', 'votos': 0},
    '18177': {'nome': 'Suely Soares', 'partido': 'REDE', 'votos': 0},
    '11789': {'nome': 'Tanilson Soares', 'partido': 'PP', 'votos': 0},
    '43146': {'nome': 'Tatiana Gomes', 'partido': 'PV', 'votos': 0},
    '22223': {'nome': 'Ten Alves da Flamengueira', 'partido': 'PL', 'votos': 0},
    '40190': {'nome': 'Tenente Coronel Viviane', 'partido': 'PSB', 'votos': 0},
    '15556': {'nome': 'Teresa Carneiro Feliciano', 'partido': 'MDB', 'votos': 0},
    '13456': {'nome': 'Teresinha Dantas', 'partido': 'PT', 'votos': 0},
    '18008': {'nome': 'Theus Carvalho', 'partido': 'REDE', 'votos': 0},
    '40000': {'nome': 'Tiberio Limeira', 'partido': 'PSB', 'votos': 0},
    '15333': {'nome': 'Toinho Nascimento', 'partido': 'MDB', 'votos': 0},
    '15100': {'nome': 'Tovar', 'partido': 'MDB', 'votos': 0},
    '50150': {'nome': 'Ulisses Barbosa', 'partido': 'PSOL', 'votos': 0},
    '15009': {'nome': 'Val da Educação', 'partido': 'MDB', 'votos': 0},
    '13455': {'nome': 'Valdenicio da Fetraf', 'partido': 'PT', 'votos': 0},
    '11100': {'nome': 'Valdilene Queiroz', 'partido': 'PP', 'votos': 0},
    '15444': {'nome': 'Vitor Hugo', 'partido': 'MDB', 'votos': 0},
    '22123': {'nome': 'Vitor Ribeiro', 'partido': 'PL', 'votos': 0},
    '80180': {'nome': 'Vitoria Ohara', 'partido': 'UP', 'votos': 0},
    '12777': {'nome': 'Wagner Nascimento', 'partido': 'PDT', 'votos': 0},
    '22111': {'nome': 'Walkíria Rocha', 'partido': 'PL', 'votos': 0},
    '22190': {'nome': 'Wallber Virgolino', 'partido': 'PL', 'votos': 0},
    '10110': {'nome': 'Wilson Filho', 'partido': 'REPUBLICANOS', 'votos': 0},
    '40011': {'nome': 'Wiviane Paiva', 'partido': 'PSB', 'votos': 0},
    '11666': {'nome': 'Zé Aldemir', 'partido': 'PP', 'votos': 0},
    '50777': {'nome': 'Zé de Dunco', 'partido': 'PSOL', 'votos': 0},
    '15151': {'nome': 'Zé do Mutirão', 'partido': 'MDB', 'votos': 0},
    '22654': {'nome': 'Zé Medeiros', 'partido': 'PL', 'votos': 0},
    '10555': {'nome': 'Zezé', 'partido': 'REPUBLICANOS', 'votos': 0},
}

candidatos_senador_vaga1 = {
    '290': {'nome': 'Adriano Trajano', 'partido': 'PCO', 'votos': 0},
    '151': {'nome': 'André Gadelha', 'partido': 'MDB', 'votos': 0},
    '222': {'nome': 'Dr. Marcelo Queiroga', 'partido': 'PL', 'votos': 0},
    '400': {'nome': 'João Azevêdo', 'partido': 'PSB', 'votos': 0},
    '801': {'nome': 'João Batista', 'partido': 'UP', 'votos': 0},
    '300': {'nome': 'Major Fábio', 'partido': 'Novo', 'votos': 0},
    '100': {'nome': 'Nabor', 'partido': 'Republicanos', 'votos': 0},
    '272': {'nome': 'Rinaldo Júnior', 'partido': 'DC', 'votos': 0},
    '800': {'nome': 'Rosilene Santana', 'partido': 'UP', 'votos': 0},
    '155': {'nome': 'Veneziano', 'partido': 'MDB', 'votos': 0}
}

candidatos_senador_vaga2 = {
    '290': {'nome': 'Adriano Trajano', 'partido': 'PCO', 'votos': 0},
    '151': {'nome': 'André Gadelha', 'partido': 'MDB', 'votos': 0},
    '222': {'nome': 'Dr. Marcelo Queiroga', 'partido': 'PL', 'votos': 0},
    '400': {'nome': 'João Azevêdo', 'partido': 'PSB', 'votos': 0},
    '801': {'nome': 'João Batista', 'partido': 'UP', 'votos': 0},
    '300': {'nome': 'Major Fábio', 'partido': 'Novo', 'votos': 0},
    '100': {'nome': 'Nabor', 'partido': 'Republicanos', 'votos': 0},
    '272': {'nome': 'Rinaldo Júnior', 'partido': 'DC', 'votos': 0},
    '800': {'nome': 'Rosilene Santana', 'partido': 'UP', 'votos': 0},
    '155': {'nome': 'Veneziano', 'partido': 'MDB', 'votos': 0}
}

candidatos_governador = {
    '29': {'nome': 'Camilo Duarte', 'partido': 'PCO', 'votos': 0},
    '15': {'nome': 'Cícero Lucena', 'partido': 'MDB', 'votos': 0},
    '22': {'nome': 'Efraim Filho', 'partido': 'PL', 'votos': 0},
    '11': {'nome': 'Lucas Ribeiro', 'partido': 'PP', 'votos': 0},
    '27': {'nome': 'Pedro Coutinho', 'partido': 'DC', 'votos': 0},
    '80': {'nome': 'Yuri Ezequiel', 'partido': 'UP', 'votos': 0}
}

candidatos_presidente = {
    '27': {'nome': 'Clariana Barão', 'partido': 'DC', 'votos': 0},
    '21': {'nome': 'Edmilson Costa', 'partido': 'PCB', 'votos': 0},
    '22': {'nome': 'Flávio Bolsonaro', 'partido': 'PL', 'votos': 0},
    '16': {'nome': 'Hertz Dias', 'partido': 'PSTU', 'votos': 0},
    '13': {'nome': 'Lula', 'partido': 'PT', 'votos': 0},
    '28': {'nome': 'Pablo Marçal', 'partido': 'PRTB', 'votos': 0},
    '14': {'nome': 'Renan Santos', 'partido': 'Missão', 'votos': 0},
    '30': {'nome': 'Romeu Zema', 'partido': 'NOVO', 'votos': 0},
    '55': {'nome': 'Ronaldo Caiado', 'partido': 'PSD', 'votos': 0},
    '29': {'nome': 'Rui Costa Pimenta', 'partido': 'PCO', 'votos': 0},
    '80': {'nome': 'Samara Martins', 'partido': 'UP', 'votos': 0},
    '70': {'nome': 'Augusto Cury', 'partido': 'Avante', 'votos': 0},
    '35': {'nome': 'Wilson Grassi', 'partido': 'Democrata', 'votos': 0}
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_numero(cargo, numero):
    qtd_digitos = {
    'deputado_federal': 4,
    'deputado_estadual': 5,
    'senador': 3,
    'governador': 2,
    'presidente': 2
    }
    return len(numero) == qtd_digitos[cargo]

def votar(cargo, candidatos, digitos):
    while True:
        numero = input(f'\n{cargo.upper()}\nDigite o número do candidator ou ENTER para branco: ')

        if numero == '':
            print('Voto em branco')
            escolha = int(input('1 - CONFIRMA\n'
                                        '2 - CORRIGE\n'
                                        '-> '))
            if escolha == 1:
                time.sleep(1)
                limpar_tela()
                return None
            if escolha == 2:
                time.sleep(1)
                limpar_tela()
                continue
        
        if not validar_numero(cargo, numero):
            print(f'Número inválido! Digite {digitos} dígitos')
            time.sleep(1)
            limpar_tela()
            continue
        
        if numero not in candidatos:
            print('Candidato não encontrado. Tente novamente')
            time.sleep(1)
            limpar_tela()
            continue

        candidato = candidatos[numero]
        print(f'Nome: {candidato["nome"]}')
        print(f'Número: {numero}')
        print(f'Partido: {candidato["partido"]}')

        escolha = int(input('1 - CONFIRMA\n'
                            '2 - CORRIGE\n'
                            '-> '))
        if escolha == 1:
            time.sleep(1)
            limpar_tela()
            return numero
        if escolha == 2:
            time.sleep(1)
            limpar_tela()
            continue

        return numero

brancos = {
    'deputado_federal': 0,
    'deputado_estadual': 0,
    'senador1': 0,
    'senador2': 0,
    'governador': 0,
    'presidente': 0
}

voto_dep_federal = votar('deputado_federal', candidatos_deputado_federal, 4)
voto_dep_estadual = votar('deputado_estadual', candidatos_deputado_estadual, 5)
voto_senador1 = votar('senador', candidatos_senador_vaga1, 3)
voto_senador2 = votar('senador', candidatos_senador_vaga2, 3)
voto_governador = votar('governador', candidatos_governador, 2)
voto_presidente = votar('presidente', candidatos_presidente, 2)

if voto_dep_federal is not None:
    candidatos_deputado_federal[voto_dep_federal]['votos'] += 1
else:
    brancos['deputado_federal'] += 1

if voto_dep_estadual is not None:
    candidatos_deputado_estadual[voto_dep_estadual]['votos'] += 1
else:
    brancos['deputado_estadual'] += 1

if voto_senador1 is not None:
    candidatos_senador_vaga1[voto_senador1]['votos'] += 1
else:
    brancos['senador1'] += 1

if voto_senador2 is not None:
    candidatos_senador_vaga2[voto_senador2]['votos'] += 1
else:
    brancos['senador2'] += 1

if voto_governador is not None:
    candidatos_governador[voto_governador]['votos'] += 1
else:
    brancos['governador'] += 1

if voto_presidente is not None:
    candidatos_presidente[voto_presidente]['votos'] += 1
else:
    brancos['presidente'] += 1

def apurar(nome_cargo, candidatos, brancos_do_cargo):
    vencedor = None
    qtd_votos = -1

    print(f'Resultado: {nome_cargo}')

    for numero_candidato, dados in candidatos.items():
        print(f"{dados['nome']} ({numero_candidato} - {dados['partido']}): {dados['votos']} votos")

        if dados['votos'] > qtd_votos:
            qtd_votos = dados['votos']
            vencedor = dados['nome']

    print(f'Brancos: {brancos_do_cargo}')
    print(f'Vencedor: {vencedor} com {qtd_votos} votos')

apurar('Deputado Federal',candidatos_deputado_federal, brancos['deputado_federal'])
apurar('Deputado Estadual',candidatos_deputado_estadual, brancos['deputado_estadual'])
apurar('Senador 1º vaga',candidatos_senador_vaga1, brancos['senador1'])
apurar('Senador 2º vaga',candidatos_senador_vaga2, brancos['senador2'])
apurar('Governador',candidatos_governador, brancos['governador'])
apurar('Presidente',candidatos_presidente, brancos['presidente'])
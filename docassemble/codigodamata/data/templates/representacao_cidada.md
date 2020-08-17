Excelentíssimo Senhor Promotor de Justiça com atribuição ambiental no Município de   **${municipio}**, Estado de **${uf}**
                   
&nbsp;
&nbsp;
&nbsp;                   
&nbsp;
&nbsp;
&nbsp;                  
&nbsp;
&nbsp;
&nbsp;                   
&nbsp;

Nos termos do art. 225, caput, da Constituição Federal e art. 70, §§ 2º e 3º, venho pelo presente levar ao conhecimento desse órgão a ocorrência, em tese, de ilícito ambiental conforme a seguir relatado.

&nbsp;                   
&nbsp;

# DOS FATOS
Trata-se de **${tipo_dano_ambiental}** ocorrido em **${data_fato}**, no local **${local_fato}**, no  município de **${municipio}**, **${uf}** 
% if possui_coordenadas:
nas proximidades das coordenadas geográficas **${coordenadas}**.
% else:
.
% endif

O fato chegou ao meu conhecimento da seguinte maneira: ${modo_conhecimento_dano_ambiental}.


% if AREA_DESTRUIDA:
A área destruída é de ${area_destruida}
% endif

% if AREA_IMOVEL:
A área do imóvel é ${area_imovel}
% endif

% if NUMERO_CAR:
A inscrição do imóvel no CAR é ${numero_car}
% endif

% if DOC_COMPROVA_FATO or LINK_DOCUMENTO_ONLINE:
Elementos de informação adicionais:
${doc_comprova_fato}
${link_documento_online}
% endif %

% if conhecimento_autoria:
Informações adcionais sobre a autoria dos fatos:
${informacoes_compl_autoria}
% endif %

&nbsp;
&nbsp;

# DO DIREITO

Sabe-se que a responsabilidade civil pela reparação do dano ambiental é objetiva na modalidade de risco integral (art. 2º, § 2º, Lei n. 12.651/2012), sendo a obrigação decorrente do referido dano solidária, propter rem e imprescritível.

O teor do enunciado de Súmula 618 do Superior Tribunal de Justiça, aprovada em 24 de outubro, dispondo que "A inversão do ônus da prova aplica-se às ações de degradação ambiental."

A evolução tecnológica dos sistemas de imagens de satélite e reconhecimento de padrões (machine learning), aliada aos princípios da prevenção e precaução, impõe a adoção, pelo Estado, de medidas imediatas para coibir, em tempo próximo ao real, dano irreversível ao meio ambiente, ainda que não se tenha absoluta certeza de ilícito quando do recebimento de alertas (com grau de precisão de 80% a 90%).

Além disso, o desmatamento ilegal e as queimadas constituem a maior causa de emissões brasileiras de gases que contribuem para o aquecimento global e a mudança climática (de consequências ainda imprevisíveis para a economia, a natureza e a sociedade).

O artigo 225 da Constituição Federal que dispõe que "Todos têm direito ao meio ambiente ecologicamente equilibrado, bem de uso comum do povo e essencial à sadia qualidade de vida, impondo-se ao Poder Público e à coletividade o dever de defendê-lo e preservá-lo para as presentes e futuras gerações."

O art. 70 da Lei n. 9.605/98 traz as seguintes disposição:

> *Art. 70. Considera-se infração administrativa ambiental toda ação ou omissão que viole as regras jurídicas de uso, gozo, promoção, proteção e recuperação do meio ambiente.*

> (...)

> *§ 2º Qualquer pessoa, constatando infração ambiental, poderá dirigir representação às autoridades relacionadas no parágrafo anterior, para efeito do exercício do seu poder de polícia.*

> *§ 3º A autoridade ambiental que tiver conhecimento de infração ambiental é obrigada a promover a sua apuração imediata, mediante processo administrativo próprio, sob pena de co-responsabilidade.*

% if solicitacao_anonimato:
${justificativa_anonimato}
% endif

&nbsp;
&nbsp;

# CONCLUSÃO

Ante o exposto, o ora comunicante requer providências para apuração do fato em questão.

 
${cidade}, ${data_hoje}

&nbsp;
&nbsp;

% if solicitacao_anonimato:
**Informante do Bem anônimo**
% else:
${subscritor}
% endif
 

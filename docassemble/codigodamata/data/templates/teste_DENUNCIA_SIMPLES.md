
${indentation} O Ministério Público, com fundamento nas normas constitucionais e legais vigentes e nos elementos colhidos no  procedimento investigatório em epígrafe, vem à presença de Vossa Excelência oferecer **DENÚNCIA** em desfavor de

&nbsp;

&nbsp;

% for  requerido in requeridos:
> **${requerido.name.full()}**, ${requerido.qualificacao}

&nbsp;

&nbsp;


% endfor

&nbsp;

&nbsp;


pela prática, em tese, dos seguintes fatos delituosos:

&nbsp;
&nbsp;

% for  fato in fatos:
**Da infração penal prevista no ${fato.fundamento_normativo}**

${indentation}  ${fato.descricao_espaco_tempo} o requerido
% for  requerido in requeridos:
> **${requerido.name.full()}**,
% endfor
${fato.descricao_fatica};

&nbsp;
&nbsp;

${indentation}  ${fato.noticia_crime}

&nbsp;
&nbsp;

${indentation} ${fato.diligencia_realizada}

&nbsp;
&nbsp;

${indentation} ${fato.paragrafo_materialidade}

&nbsp;
&nbsp;

${indentation} ${fato.representacao}.

&nbsp;
&nbsp;

% endfor

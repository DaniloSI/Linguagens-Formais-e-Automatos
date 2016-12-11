[condition][]Existe um ou mais politicos honestos=exists( Politico( honesto == true ) )
[condition][]Se existir uma esperanca=exists( Esperanca() )
[condition][]Se nao existir uma esperanca=not( Esperanca() )
[condition][]Houver um conjunto de politicos honestos=$politico : Politico( honesto == true )


[consequence][]Existe uma experanca=insertLogical( new Esperanca() );
[consequence][]Diga que a esperanca esta viva=System.out.println("Hurrah!!! A democracia vive!");
[consequence][]Diga que a democracia esta morta=System.out.println( "Estamos todos condenados!!! A democracia esta morta." );
[consequence][]A corporacao do mal corrompe os politicos=System.out.println( "Eu sou uma corporacao do mal e tenho corrompido o(a) " + $politico.getNome() );modify( $politico ) \{ setHonesto( false ) \}
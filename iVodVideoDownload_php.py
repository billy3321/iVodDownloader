#   - * -   c o d i n g :   u t f - 8   - * -  
 # i V o d q_GrN	�h a n d l e r  
 i m p o r t   u r l l i b 2 , s y s , r e , o s , p l a t f o r m , s u b p r o c e s s   a s   s p  
 f r o m   P y Q t 4 . Q t G u i   i m p o r t   *    
 f r o m   P y Q t 4 . Q t C o r e   i m p o r t   *    
 r e l o a d ( s y s )  
 s y s . s e t d e f a u l t e n c o d i n g ( ' u t f 8 ' )  
 # �_��f9e�pp h p �v�[݈�v� 
 i f   p l a t f o r m . s y s t e m ( )   = = ' W i n d o w s ' :  
         p h p E x e c u t i o n P a t h   =   ' C : / U s e r s / c y u 3 / D o w n l o a d s / p h p - 5 . 5 . 3 2 - W i n 3 2 - V C 1 1 - x 8 6 / p h p . e x e '  
  
 e l i f   p l a t f o r m . s y s t e m ( )   = = ' D a r w i n ' :  
         # M a c   h a s   b u i l l d   i n   p h p  
         p h p E x e c u t i o n P a t h   =   ' p h p '  
  
 e l s e :  
         # L i n u x  
         p h p E x e c u t i o n P a t h   = ' p h p '  
  
 # 8�eQ�Sxe 
 # a r g U R L a n d F i l e N a m e L i s t   l i s t [ s t r , s t r ]   #     N	�MOn  �T  �jT  L i s t [ U R L , F i l e N a m e ]  
 # a r g S a v e F o l d e r   :   s t r   #   N	��v� 
 # a r g H D   :   b o o l e a n   #   /f&TN	�ؚku� 
 # a r g Q T S t a t u s   :   Q T e x t B r o w s e r   #   o�:y2��^�v�c6R� 
 c l a s s   i V o d V i d e o D o w n l o a d ( Q M a i n W i n d o w ) :  
         d e f   _ _ i n i t _ _ ( s e l f ,   a r g U R L a n d F i l e N a m e L i s t ,   a r g S a v e F o l d e r ,   a r g H D ,   a r g Q T S t a t u s ) :  
                 i f   n o t   s e l f . h a s P H P ( p h p E x e c u t i o n P a t h ) :  
                       r a i s e   E x c e p t i o n ( " C a n ' t   f i n d   P H P ;   p l e a s e   i n s t a l l   P H P   a n d   c h a n g e   l o c a t i o n   a b o v e " )  
                 Q W i d g e t . _ _ i n i t _ _ ( s e l f )  
                 s e l f . S a v e F o l d e r   =   a r g S a v e F o l d e r  
                 s e l f . Q t S t a t u s   =   a r g Q T S t a t u s  
                 s e l f . M a n i f e s t   =   [ ]  
                 s e l f . h e a d e r     = { ' U s e r - a g e n t ' :   ' M o z i l l a / 5 . 0   ( X 1 1 ;   L i n u x   x 8 6 _ 6 4 )   A p p l e W e b K i t / 5 3 7 . 3 6   ( K H T M L ,   l i k e   G e c k o )   C h r o m e / 3 5 . 0 . 1 9 1 6 . 1 5 3   S a f a r i / 5 3 7 . 3 6 ' }  
                 f o r   U R L A n d F i l e N a m e   i n   a r g U R L a n d F i l e N a m e L i s t :  
                         U R L   =   U R L A n d F i l e N a m e [ 0 ]  
                         F i l e N a m e   =   a r g S a v e F o l d e r   +   " / "   +   U R L A n d F i l e N a m e [ 1 ]  
                         i f   a r g H D :  
                                 U R L =   s t r ( U R L A n d F i l e N a m e [ 0 ] ) . r e p l a c e ( ' 3 0 0 K ' , ' 1 M ' )  
                         # �j�gU R L 6q�_�bǌ�e 
                         i f   U R L   ! =   ' ' :                                          
                                 h t m l   = u r l l i b 2 . u r l o p e n ( u r l l i b 2 . R e q u e s t ( U R L , N o n e , s e l f . h e a d e r ) ) . r e a d ( )  
                         # F i n d   R e a l U R L  
                         # r e a d y P l a y e r ( ' h t t p : / / i v o d . l y . g o v . t w / p u b l i c / s c r i p t s / ' , ' h t t p : / / h 2 6 4 m e d i a 0 1 . l y . g o v . t w : 1 9 3 5 / v o d / _ d e f i n s t _ / m p 4 : 1 M C l i p s / a 7 d 6 0 2 7 a 1 d e d 6 a a 6 6 2 3 7 e 8 9 5 a 7 b 3 5 4 3 0 9 c 4 5 0 e 4 5 0 7 4 0 c f 3 0 d a 2 b 7 6 0 e 9 3 2 7 b 2 f d a 0 4 1 c a e 0 9 2 e 7 6 4 1 7 . m p 4 / m a n i f e s t . f 4 m ' ) ;  
                         m a t c h _ r e a d y p l a y e r   =   r e . f i n d a l l ( r " r e a d y P l a y e r \ ( ' . * \ ) " , h t m l )                        
                          
                         m a n i f e s t _ u r l   =   r e . f i n d a l l ( r " , \ ' . * \ ) " ,   m a t c h _ r e a d y p l a y e r [ 0 ] ) [ 0 ] [ 2 : - 2 ]  
                         m a n i f e s t _ h t m l   = u r l l i b 2 . u r l o p e n ( u r l l i b 2 . R e q u e s t ( m a n i f e s t _ u r l , N o n e , s e l f . h e a d e r ) ) . r e a d ( )  
                          
                         d u r a t i o n _ s e c   =   r e . f i n d a l l ( r ' < d u r a t i o n > . * < '   , m a n i f e s t _ h t m l ) [ 0 ] [ 1 0 : - 2 ]  
                         d u r a t i o n _ m i n   =   f l o a t ( d u r a t i o n _ s e c ) /   6 0 . 0                          
                         t e m p F i l e N a m e   =   a r g S a v e F o l d e r + " / t m p . f l v "  
                         s e l f . M a n i f e s t . a p p e n d ( [ U R L , m a n i f e s t _ u r l , F i l e N a m e ] )  
                         s e l f . p r o c e s s   = Q P r o c e s s ( s e l f )  
                         s e l f . p r o c e s s . r e a d y R e a d S t a n d a r d O u t p u t . c o n n e c t ( s e l f . d a t a R e a d y )  
                         s e l f . p r o c e s s . f i n i s h e d . c o n n e c t ( s e l f . f i n i s h )  
  
         d e f   d o w n l o a d F i l e ( s e l f ) :  
                 d o w n l o a d f a i l e d   =   [ ]  
                 f o r   m a n i f e s t   i n   s e l f . M a n i f e s t :  
                         t e m p F i l e N a m e   =   s e l f . S a v e F o l d e r   + " / t m p . f l v "  
                         F i l e N a m e   =   m a n i f e s t [ 2 ]  
                                
                         # x d o w n l o a d   =   A d o b e H D S . M 6 ( m a n i f e s t [ 1 ] , t e m p F i l e N a m e )      
                         s e l f . r u n n i n g   =   F a l s e  
                         s e l f . Q t S t a t u s . a p p e n d ( u n i c o d e ( ' N	��jT: ' )   +   F i l e N a m e )  
                         s e l f . Q t S t a t u s . a p p e n d ( u n i c o d e ( ' �S�YU R L : ' )   +   m a n i f e s t [ 0 ] )  
                         s e l f . Q t S t a t u s . a p p e n d ( u n i c o d e ( ' M a n i f e s t   U R L : ' )   +   m a n i f e s t [ 1 ] )                          
  
                         # c a l l   p h p  
                         s e l f . c a l l A d o b e H D S ( m a n i f e s t [ 1 ] , t e m p F i l e N a m e )  
                          
                         # �f�eQ T CQ�N 
                         w h i l e   s e l f . r u n n i n g :                                
                                 Q A p p l i c a t i o n . p r o c e s s E v e n t s ( )  
  
                         # �Y�g	g�fX[�jHhX[(W  N	�1YWe  *Rd��fX[�j 
                         i f   n o t   o s . p a t h . i s f i l e ( t e m p F i l e N a m e ) :  
                                 d o w n l o a d f a i l e d . a p p e n d ( F i l e N a m e )  
                                 f o r   s   i n   o s . l i s t d i r ( ' . / ' ) :  
                                         i f   s . f i n d ( ' S e g 1 - F r a g ' )   ! = - 1 :  
                                                 o s . r e m o v e ( s )  
                         # I��cN	�T1z  �	g͑��f9e�eN	�T 
                         e l s e :  
                                 w h i l e ( o s . p a t h . i s f i l e ( F i l e N a m e ) ) :  
                                         F i l e N a m e   =   F i l e N a m e [ 0 : - 4 ]   +   " _ 1 . f l v "  
                                 o s . r e n a m e ( t e m p F i l e N a m e , F i l e N a m e )  
                 i f   l e n ( d o w n l o a d f a i l e d ) ! = 0 :  
                         f o r   s   i n   d o w n l o a d f a i l e d :  
                                 s e l f . Q t S t a t u s . a p p e n d ( s   +   u '     d o w n l o a d   1YWe' )  
                          
         d e f   c a l l A d o b e H D S ( s e l f ,   m a n i f e s t U R L ,   t m p F i l e L o c a t i o n ) :  
                 s e l f . r u n n i n g   =   T r u e  
                 s e l f . p r o c e s s . s t a r t ( p h p E x e c u t i o n P a t h   , [ " A d o b e H D S _ b i l l y 3 3 2 1 . p h p " , " - - q u a l i t y " , " h i g h " , " - - u s e r a g e n t " ,   s e l f . h e a d e r [ ' U s e r - a g e n t ' ] , ' - - d e l e t e ' , ' - - o u t f i l e ' , t m p F i l e L o c a t i o n , ' - - m a n i f e s t ' , m a n i f e s t U R L ] ) # ,   s h e l l = T r u e ,   s t d o u t = s u b p r o c e s s . P I P E )  
                  
                  
         d e f   f i n i s h ( s e l f ) :                  
                 s e l f . r u n n i n g   =   F a l s e  
          
         d e f   d a t a R e a d y ( s e l f ) :  
                 c u r s o r   =   s e l f . Q t S t a t u s . t e x t C u r s o r ( )  
                 c u r s o r . m o v e P o s i t i o n ( c u r s o r . E n d )  
                 c u r s o r . i n s e r t T e x t ( s t r ( s e l f . p r o c e s s . r e a d A l l S t a n d a r d O u t p u t ( ) ) )  
                 s e l f . Q t S t a t u s . e n s u r e C u r s o r V i s i b l e ( )  
  
         d e f   h a s P H P ( s e l f ,   a r g ) :  
                 t r y :  
                         s p . c h e c k _ c a l l ( [ a r g ,   ' - v ' ] )  
                         r e t u r n   T r u e  
                 e x c e p t :  
                         r e t u r n   F a l s e  
  
 # ,nf�@SJX 
 #   g l o b a l   m a i n F o r m  
 #   d e f   b u t t o n _ c l i c k ( ) :  
 #           s t a t u s   =   m a i n F o r m . f i n d C h i l d ( Q T e x t B r o w s e r , " S t a t u s " ) ;  
 #           l i s t U R L   =   [ [ " h t t p : / / i v o d . l y . g o v . t w / P l a y / V O D / 7 6 4 7 2 / 3 0 0 K " , " t e s t . f l v " ] ]  
 #           d o w n l o a d   =   i V o d V i d e o D o w n l o a d ( l i s t U R L ,   " . / " , T r u e , s t a t u s )  
 #           d o w n l o a d . d o w n l o a d F i l e ( )  
 #  
 #   d e f   m a i n ( ) :  
 #           a p p   =   Q A p p l i c a t i o n ( s y s . a r g v )  
 #           g l o b a l   m a i n F o r m  
 #           m a i n F o r m   =   Q W i d g e t ( )  
 #           m a i n F o r m . r e s i z e ( 8 0 0 , 4 0 0 )  
 #           l a y o u t   =   Q V B o x L a y o u t ( )  
 #           e d i t   =   Q T e x t B r o w s e r ( )  
 #           e d i t . s e t O b j e c t N a m e ( " S t a t u s " )  
 #           e d i t . s e t W i n d o w T i t l e ( " Q T e x t E d i t   S t a n d a r d   O u t p u t   R e d i r e c t i o n " )  
 #           l a y o u t . a d d W i d g e t ( e d i t )  
 #           b u t t o n   =   Q P u s h B u t t o n ( )  
 #           b u t t o n . c l i c k e d . c o n n e c t ( b u t t o n _ c l i c k )  
 #           l a y o u t . a d d W i d g e t ( b u t t o n )  
 #           m a i n F o r m . s e t L a y o u t ( l a y o u t )  
 #           m a i n F o r m . s h o w ( )  
 #           a p p . e x e c _ ( )  
 #  
 #  
 #   i f   _ _ n a m e _ _   = =   ' _ _ m a i n _ _ ' :  
 #           m a i n ( ) 
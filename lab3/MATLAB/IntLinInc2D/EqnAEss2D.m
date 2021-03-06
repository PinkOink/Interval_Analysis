function [V,P1,P2,P3,P4]=EqnAEss2D(infA,supA,Aq,infb,supb,bq)
%
% The function  EqnAEss2D  visualizes  AE-solution set 
% for the system of interval linear equations  A x = b, where
%   A  is an interval matrix with  m  rows and  2 columns,
%   b  is an interval vector of the length  m.
%
% Input arguments:
% infA, supA  are  left and right endpoints of the interval matrix  A  
%   respectively;
% Aq is a quantifier matrix with  m  rows and  2 columns, 
%   its elements are letters 'A' and 'E', which correspond to universality 
%   and existence quantifiers in the description of the AE-solution;
% infb, supb  are  left and right endpoints of the interval vector  b  
%   respectively;
% bq is a quantifier vector of the length  m, whose elements are letters 
%   'A' and 'E' (similar to  Aq).
%
% Output arguments:
% V is a matrix of orientation points.
%   In the package, the orientation points are understood as vertices 
%   of intersections of the solution set with orthants.
% Pk, k=1,2,3,4.
%   If intersection of the solution set with the k-th orthant is bounded,
%   Pk is a closed clockwise path around the piece of the solution set 
%   in the k-th orthant. 
%   Otherwise, Pk is the same path but constructed around intersection 
%   of the cut box B with the piece of the solution set in the k-th orthant. 
%   The program chooses the cut box  B  automatically.
%
% Written by Irene A. Sharaya (Institute of Computational Technologies, Novosibirsk)
% Date:  March 7, 2012

    % turn to interval inclusion [uC,oC] x \subseteq [ud,od] 
    % in Kaucher arithmetic
    m=size(infA,1);
    uC=infA; 
    oC=supA;
    Aqe=[Aq==ones(m,2)*'E'];
    uC(Aqe)=supA(Aqe);
    oC(Aqe)=infA(Aqe);
    ud=infb; 
    od=supb; 
    bqa=[bq==ones(m,1)*'A'];
    ud(bqa)=supb(bqa);
    od(bqa)=infb(bqa);

    % visualize the solution set 
    % to the inclusion [uC,oC] x \subseteq [ud,od]
    % and, if necessary, display V and Pk (k=1,2,3,4)
    if nargout < 1
        Cxind2D(uC,oC,ud,od);
    end
    if nargout == 1
        [V]=Cxind2D(uC,oC,ud,od);
    end
    if nargout > 1
        [V,P1,P2,P3,P4]=Cxind2D(uC,oC,ud,od);
    end

end

function [alphalim] = AlphaLimit(xmin,x,xmax,d)

% This function finds the allowable limits of alpha when vector alpha*d originating
% at point x must be limited within the box constraints xmin and xmax
alphalim[1] = min((xmax-x)/d);
alphalim[2] = max((x-xmin)/d);

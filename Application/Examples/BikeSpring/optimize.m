function [x] = optimize(xmin,x,xmax,maxiter)

% Finds the minimum of a function of N variables using Bremermann's method
%
% Input:
% x...........Initial guess (vector of N elements)
% maxiter.....Stops when no improvent occurs for this many iterations

% Output:
% x...........Estimate of the minimum

% start iteration loop
i = 0;
while i<maxiter
    d = randn(size(x));
    golden(x,d);
end

function [x F] = golden(xmin,x,xmax,d,niter)

% Minimizes the objetive function in the direction of d by the golden section
% method. This handles functions with any degree of non-smoothness
% with the only assumption that the function is unimodal, i.e. it
% has a single minimum in the interval

% Input:
% xmin........Lower bound for x
% x...........Current design point
% xmax........Upper bound for x
% d...........Search vector
% niter.......Number of iterations to perform

% Output:
% x...........Updated design variable vector
% F...........Associated objective function value

% Find the limit of alpha within the box constraints xmin and xmax
golden = 0.618;
B = 1.0e10;
bb = 1.0e10;
for j=1:length(x)
    if d(j)>0
        bb = (xmax(j)-x(j))/d(j);
    end
    if d(j)<0
        bb = (xmin(j)-x(j))/d(j);
    end;
    B = min(B,bb);
end
B = 1.1*B;  % Extend a little to allow the exterior penalty to work
A = 0;      % Left interval end. Always zero because we have a search direction

% Compute initial golden section points and their function values
alpha1 = B-(B-A)*golden;
alpha2 = A+(B-A)*golden;
F1 = ObjectivePenal(xmin,x+alpha1*d,xmax);
F2 = ObjectivePenal(xmin,x+alpha2*d,xmax);
for i=1:niter
    if (F1 <= F2)
        B = alpha2;
        alpha2 = alpha1;
        F2 = F1;
        alpha1 = B - (B-A)*golden;
        F1 = ObjectivePenal(xmin,x+alpha1*d,xmax);
    else
        A = alpha1;
        alpha1 = alpha2;
        F1 = F2;
        alpha2 = A + (B-A)*golden;
        F2 = ObjectivePenal(xmin,x+alpha2*d,xmax);
    end
end

% Update design variable vector
x = x+alpha1*d;
F = F1;

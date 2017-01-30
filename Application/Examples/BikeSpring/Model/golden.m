function [x, F] = golden(xmin,x,xmax,d,niter)

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

% Find limits of alpha within the box constraints xmin and xmax
golden = 0.618;
A = -1.0e10;
B = 1.0e10;
aa = -1.0e10;
bb = 1.0e10;
for j=1:length(x)
    if d(j)>0
        aa = (xmin(j)-x(j))/d(j);
        bb = (xmax(j)-x(j))/d(j);
    end
    if d(j)<0
        aa = (xmax(j)-x(j))/d(j);
        bb = (xmin(j)-x(j))/d(j);
    end;
    A = max(A,aa);
    B = min(B,bb); % extend a bit to allow the peanlty to work
end

% Compute initial golden section points and their function values
alpha1 = B-(B-A)*golden;
alpha2 = A+(B-A)*golden;
F1 = objective(x+alpha1*d);
F2 = objective(x+alpha2*d);
for i=1:niter
    if (F1 <= F2)
        B = alpha2;
        alpha2 = alpha1;
        F2 = F1;
        alpha1 = B - (B-A)*golden;
        F1 = objective(x+alpha1*d);
    else
        A = alpha1;
        alpha1 = alpha2;
        F1 = F2;
        alpha2 = A + (B-A)*golden;
        F2 = objective(x+alpha2*d);
    end
end

% Update design variable vector
x = x+alpha1*d;
F = F1;

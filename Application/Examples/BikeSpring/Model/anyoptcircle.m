function B = anyopt
% Unconstrained optimization in the AnyBody Modeling System
% using a golden section method with circular directions
% along parameter axes

% Design variables as they appear in the AnyScript model
    % AnyVar L0 = 0.24;             //Spring slack length
    % AnyVar F1 = 100;              //Spring force at 50% strain
    % AnyVar SpringRad = 0.15;      //Radius of spring attachment on the crank
    % AnyVar SpringAngle = 45;      //Angle of spring attachment points on the crank
    % AnyVar SpringX = -0.10;       //X coordinate of spring attachment on frame
    % AnyVar SpringY = 0.30
    
% Initialize 
%        L0        F1    SpringRad  SpringAngle   SpringY
xmin = [0.05       0.0      0.01        0.0        0.1];   % Lower bound
x =    [0.1009     0.0     0.1104     61.65      0.1012];   % Initial guess
%x =    [0.0112  175.3446    0.1116   64.0230     0.1012]; Optimized
xmax = [0.4     1000.0      0.40      180.0         0.5];   % Upper bound

% do optimization
maxiter = 10;
evals = 0;   % Counter of function evaluations
delta = 0.1;  % Relative perturbation
gradindex = 1; % Index of variable to minimize along

while evals<maxiter*length(x)
    
    for j=1:length(x) 
        d(j) = 0.0;
    end
    d(gradindex) = 1;
    [x F] = golden(xmin,x,xmax,d,10)    % Perform golden section optimization in that direction
    if gradindex==length(x)
        gradindex=1;
        [evals F]
        pause;
    else
        gradindex = gradindex + 1;
    end
    evals = evals + 1;
end
F

% Systematic variation of two parameters

% Design variables as they appear in the AnyScript model
    % AnyVar L0 = 0.24;             //Spring slack length
    % AnyVar F1 = 100;              //Spring force at 50% strain
    % AnyVar SpringRad = 0.15;      //Radius of spring attachment on the crank
    % AnyVar SpringAngle = 45;      //Angle of spring attachment points on the crank
    % AnyVar SpringX = -0.10;       //X coordinate of spring attachment on frame
    % AnyVar SpringY = 0.30
    
% Initialize 
%        L0        F1    SpringRad  SpringAngle  SpringY
xmin = [0.1       0.0      0.01        0.0         0.1];   % Lower bound
x =    [0.2897  114.5789    0.1673   49.2547    0.4311];   % Initial guess
xmax = [0.4    1000.0      0.40      180.0         0.5];   % Upper bound

% Variable choice
n1 = 4;
n2 = 5;
nStep = 8;

% Initialize temporary variable xx
d1 = (xmax(n1)-xmin(n1))/(nStep-1);
d2 = (xmax(n2)-xmin(n2))/(nStep-1);

% Fill abscissa arrays
for i=0:nStep-1
    p1(i+1) = xmin(n1) + i*d1;
    p2(i+1) = xmin(n2) + i*d2;
end

% Fill ordinate array
count = 1;
xx = x;
for i=1:nStep
    xx(n1) = p1(i);
    for j=1:nStep
        xx(n2) = p2(j);
        result(i,j) = objective(xx);
        count = count + 1;
    end
end
 
%Plotting
surf(p1,p2,result);
 
clear;

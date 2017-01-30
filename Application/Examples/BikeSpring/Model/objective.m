function [F] = objective(x)

F = 0;

%  AnyVar L0 = 0.24;             //Spring slack length
%  AnyVar F1 = 100;               //Spring force at 50% strain
%  AnyVar SpringRad = 0.15;      //Radius of spring attachment on the crank
%  AnyVar SpringAngle = 45;      //Angle of spring attachment points on the crank
%  AnyVar SpringX = -0.10;       //X coordinate of spring attachment on frame
%  AnyVar SpringY = 0.30;        //Y coordinate of spring attachment on frame

% Create include file with variable values
fid=fopen('AnyInc.any','wt');
fprintf(fid,'AnyVar L0 = %12.4f;\n',x(1));
fprintf(fid,'AnyVar F1 = %12.4f;\n',x(2));
fprintf(fid,'AnyVar SpringRad = %12.4f;\n',x(3));
fprintf(fid,'AnyVar SpringAngle = %12.4f;\n',x(4));
fprintf(fid,'AnyVar SpringX = %12.4f;\n',0.0);   % Taken out of the problem
fprintf(fid,'AnyVar SpringY = %12.4f;\n',x(5));
fclose(fid);

fprintf(1,'\n			Running simulation...\n');
dos('anybodycon springeval.anymcr');
%[s,w]=dos('c:\program files\anybody\anybodycon springeval.anymcr');
%while ans~=0%length(w)<5747
%  pause(1)
%end

Data = csvread('MaxActivity.csv',13,0);
time = Data(:,1);
b = Data(:,2);     
F=max(b);

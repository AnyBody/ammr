data = DistPhalanx;

x = data(:,2);
y = data(:,3);
z = data(:,4);
N = length(x);          
n = 0:N-1; 

top = max(data(:,4));
bottom = max(data(:,4));

% Fast Fourier transform
S=fft(x);

figure (1);

% Signal in Time domain
subplot(4,1,1);
plot(n,x);
axis([0,295,-200,top*1.1]);

% Signal in frequence domain
subplot(4,1,2);
plot(n,S);
axis([0,295,-inf,inf]);

% Determination of order and corresponding cutoff frequency
% SPECIFICATIONS: DC-gain: 0 dB, Passband: 0<f<33 Hz,
% Maximum ripple in the passband: 1 dB, Stopband: f>50 Hz
% Stopband attenuation > 40 dB, Sample frequency: 1000 Hz
[N, Wn] = BUTTORD(3/120, 12/120, 1, 40);

% Determination of the filter coefficients 
[B,A] = BUTTER(N,Wn);

% Returns the frequency response vector h and the corresponding 
% frequency vector w for the filter with coefficients A, B
[Hz,w]=freqz(B,A); 

% Plot of frequency response
subplot(4,1,3);
plot(w,abs(Hz));
axis([0 1 0 1]);

% Filter
X = filtfilt(B,A,x);
Y = filtfilt(B,A,y);
Z = filtfilt(B,A,z);


dataFilt(:,1) = Scapula1(:,1);
dataFilt(:,2) = X;
dataFilt(:,3) = Y;
dataFilt(:,4) = Z;

figure(2)
Subplot(2,3,1)
plot (data(1:295,2)); figure(gcf)
Subplot(2,3,2)
plot (data(1:295,3)); figure(gcf)
Subplot(2,3,3)
plot (data(1:295,4)); figure(gcf)

Subplot(2,3,4)
plot (dataFilt(1:295,2)); figure(gcf)
Subplot(2,3,5)
plot (dataFilt(1:295,3)); figure(gcf)
Subplot(2,3,6)
plot (dataFilt(1:295,4)); figure(gcf)


figure(3)
subplot(2,2,1)
plot(data(1:295,4))
subplot(2,2,3)
plot(dataFilt(1:295,4))
subplot(2,2,2)
plot(data(195:220,4))
subplot(2,2,4)
plot(dataFilt(195:220,4))

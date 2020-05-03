import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {environment} from '../environments/environment';
import {ContainerOperation, SingleContainerOperation} from '../interfaces/container';
import {ImageOperation, SingleImageOperation} from '../interfaces/image';

@Injectable({
  providedIn: 'root'
})
export class DeployService {
  path = '/api/deploy';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService
  ) { }

  containerOperation(containerOperation: ContainerOperation): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/container', {
        ...containerOperation
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  singleContainerOperation(singleContainerOperation: SingleContainerOperation): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/container/single', {
        ...singleContainerOperation
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  imageOperation(imageOperation: ImageOperation): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/image', {
        ...imageOperation
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  singleImageOperation(singleImageOperation: SingleImageOperation): Observable<any> {
    return this.httpClient.post(environment.backendUrl + this.path + '/image/single', {
        ...singleImageOperation
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}

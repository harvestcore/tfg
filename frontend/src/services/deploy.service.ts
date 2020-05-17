import {HttpClient} from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';

import {AuthService} from './auth.service';
import {ContainerOperation, SingleContainerOperation} from '../interfaces/container';

import {ImageOperation, SingleImageOperation} from '../interfaces/image';
import {UrlService} from './url.service';

@Injectable({
  providedIn: 'root'
})
export class DeployService {
  path = '/api/deploy';

  constructor(
    private httpClient: HttpClient,
    private authService: AuthService,
    private urlService: UrlService
  ) { }

  containerOperation(containerOperation: ContainerOperation): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/container', {
        ...containerOperation
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  singleContainerOperation(singleContainerOperation: SingleContainerOperation): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/container/single', {
        ...singleContainerOperation
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  imageOperation(imageOperation: ImageOperation): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/image', {
        ...imageOperation
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }

  singleImageOperation(singleImageOperation: SingleImageOperation): Observable<any> {
    return this.httpClient.post(this.urlService.getBackendUrl() + this.path + '/image/single', {
        ...singleImageOperation
      }, {
        headers: this.authService.getXAccessTokenHeader()
      }
    );
  }
}
